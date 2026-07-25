"""Shablonlardan msgid larni ajratib, JSON tarjimalardan .po va .mo yaratadi.

Windows'da GNU gettext (`xgettext`, `msgfmt`) o'rnatilmagan bo'lishi mumkin,
shuning uchun `makemessages`/`compilemessages` o'rniga shu buyruq ishlatiladi.
Tarjimalar oddiy JSON lug'atlarida saqlanadi: {"msgid": "msgstr"}.
Bir tilning tarjimalari `locale/translations/<til>/` ichidagi bir nechta
JSON faylga bo'lib qo'yilishi mumkin — ular birlashtiriladi.

Ishlatish:
    python manage.py buildmessages
    python manage.py buildmessages --check   (faqat hisobot, fayl yozmaydi)
"""
import json
import re
from datetime import datetime, timezone

import polib
from django.conf import settings
from django.core.management.base import BaseCommand

# {% translate "..." %} / {% trans '...' %} — ixtiyoriy `as var` bilan
TEMPLATE_TAG = re.compile(
    r"""\{%\s*trans(?:late)?\s+(?P<quote>["'])(?P<text>.*?)(?<!\\)\1"""
    r"""(?:\s+as\s+\w+)?\s*%\}""",
    re.S,
)
# {% blocktranslate %}...{% endblocktranslate %} — HTML saqlanadigan matnlar uchun
TEMPLATE_BLOCK = re.compile(
    r"\{%\s*blocktrans(?:late)?\s*(?P<flags>[^%]*?)%\}(?P<text>.*?)\{%\s*endblocktrans(?:late)?\s*%\}",
    re.S,
)
# Python: _("...") yoki gettext_lazy('...')
PYTHON_CALL = re.compile(
    r"""\b(?:_|gettext|gettext_lazy|pgettext)\(\s*(?P<quote>["'])(?P<text>.*?)(?<!\\)\1\s*[),]""",
    re.S,
)


class Command(BaseCommand):
    help = "Shablonlardan msgid larni ajratib, .po va .mo fayllarini yaratadi"

    def add_arguments(self, parser):
        parser.add_argument(
            '--check',
            action='store_true',
            help="Fayllarni yozmasdan, yetishmayotgan tarjimalar hisobotini chiqaradi",
        )

    def handle(self, *args, **options):
        base_dir = settings.BASE_DIR
        locale_dir = base_dir / 'locale'

        msgids = self._extract_msgids(base_dir)
        locale_dir.mkdir(parents=True, exist_ok=True)
        (locale_dir / 'msgids.json').write_text(
            json.dumps(msgids, ensure_ascii=False, indent=1), encoding='utf-8'
        )

        # Yangilik matnlari, ism-familiyalar va rasmiy hujjat nomlari
        # ataylab o'zbek tilida qoldiriladi.
        notranslate_path = locale_dir / 'notranslate.json'
        notranslate = set()
        if notranslate_path.exists():
            notranslate = set(json.loads(notranslate_path.read_text(encoding='utf-8')))

        self.stdout.write(
            f"Ajratildi: {len(msgids)} noyob msgid "
            f"({len(notranslate)} tasi ataylab tarjima qilinmaydi)"
        )

        default_language = settings.LANGUAGE_CODE
        report = []

        for code, _name in settings.LANGUAGES:
            if code == default_language:
                continue

            translations = self._load_translations(locale_dir / 'translations' / code)
            expected = [msgid for msgid in msgids if msgid not in notranslate]
            missing = [msgid for msgid in expected if not translations.get(msgid)]
            extra = [msgid for msgid in translations if msgid not in msgids]

            report.append((code, len(expected), len(missing), len(extra)))

            if options['check']:
                for msgid in missing[:10]:
                    self.stdout.write(self.style.WARNING(f"  [{code}] yo'q: {msgid[:80]}"))
                continue

            self._write_catalog(locale_dir, code, msgids, translations)

        self.stdout.write('')
        for code, total, missing, extra in report:
            status = self.style.SUCCESS("to'liq") if not missing else self.style.WARNING(f"{missing} ta yo'q")
            suffix = f", {extra} ta keraksiz" if extra else ''
            self.stdout.write(f"{code}: {total - missing}/{total} tarjima - {status}{suffix}")

    def _extract_msgids(self, base_dir):
        """Shablon va Python fayllardan tarjima qilinadigan matnlarni yig'adi."""
        msgids: dict[str, list[str]] = {}

        def add(text, source):
            if not text:
                return
            msgids.setdefault(text, [])
            if source not in msgids[text]:
                msgids[text].append(source)

        for path in sorted((base_dir / 'main/templates').rglob('*.html')):
            content = path.read_text(encoding='utf-8')
            for match in TEMPLATE_TAG.finditer(content):
                add(match.group('text'), path.name)
            for match in TEMPLATE_BLOCK.finditer(content):
                text = match.group('text')
                if 'trimmed' in match.group('flags'):
                    text = ' '.join(text.split())
                if '{{' in text:
                    self.stdout.write(self.style.WARNING(
                        f"  {path.name}: blocktranslate ichidagi o'zgaruvchi qo'lda tekshirilishi kerak"
                    ))
                add(text, path.name)

        for path in sorted((base_dir / 'main').rglob('*.py')):
            if 'management' in path.parts or 'migrations' in path.parts:
                continue
            content = path.read_text(encoding='utf-8')
            for match in PYTHON_CALL.finditer(content):
                add(match.group('text'), path.name)

        return msgids

    def _load_translations(self, directory):
        """Katalogdagi barcha JSON fayllarni bitta lug'atga birlashtiradi."""
        merged = {}
        if not directory.exists():
            return merged
        for path in sorted(directory.glob('*.json')):
            data = json.loads(path.read_text(encoding='utf-8'))
            duplicates = merged.keys() & data.keys()
            if duplicates:
                self.stdout.write(self.style.WARNING(
                    f"  {path.name}: {len(duplicates)} ta takroriy kalit ustidan yozildi"
                ))
            merged.update(data)
        return merged

    def _write_catalog(self, locale_dir, code, msgids, translations):
        messages_dir = locale_dir / code / 'LC_MESSAGES'
        messages_dir.mkdir(parents=True, exist_ok=True)

        catalog = polib.POFile(check_for_duplicates=False)
        catalog.metadata = {
            'Project-Id-Version': 'Varnet Biotech University',
            'POT-Creation-Date': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M+0000'),
            'MIME-Version': '1.0',
            'Content-Type': 'text/plain; charset=UTF-8',
            'Content-Transfer-Encoding': '8bit',
            'Language': code,
        }

        for msgid, sources in msgids.items():
            entry = polib.POEntry(
                msgid=msgid,
                msgstr=translations.get(msgid, ''),
                occurrences=[(source, '') for source in sources],
            )
            catalog.append(entry)

        catalog.save(str(messages_dir / 'django.po'))
        catalog.save_as_mofile(str(messages_dir / 'django.mo'))
        self.stdout.write(f"  yozildi: locale/{code}/LC_MESSAGES/django.{{po,mo}}")
