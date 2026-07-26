# Varnet Xalqaro Biotexnologiyalar Universiteti — veb-sayt

Django asosida qurilgan universitet veb-sayti: universitet haqida ma'lumot,
tuzilma, rahbariyat, ilmiy va moliyaviy faoliyat, qabul jarayoni, yangiliklar,
e'lonlar va onlayn hujjat topshirish tizimi.

## Texnologiyalar

| Qism | Vosita |
| --- | --- |
| Backend | Django 5.2 (Python 3.12+) |
| Ma'lumotlar bazasi | SQLite (mahalliy), ishlab chiqarishda PostgreSQL tavsiya etiladi |
| Frontend | Server tomonda render qilinadigan shablonlar, mustaqil CSS/JS (framework yo'q) |
| Statik fayllar | WhiteNoise (siqilgan, manifest bilan) |
| PDF | ReportLab (universitet tuzilmasini yuklab olish) |
| Ko'p tillilik | Django i18n + polib (o'zbek, rus, ingliz, turk) |

## O'rnatish

```bash
git clone https://github.com/000Jasurbek000/VarnetBioTech.git
cd VarnetBioTech

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

Sozlama fayllarini tayyorlang. `varnet/settings.py` va `.env` git'da
saqlanmaydi — har bir kompyuter va server o'z nusxasini yuritadi:

```bash
cp varnet/settings.example.py varnet/settings.py
cp .env.example .env
```

`.env` faylida `DJANGO_SECRET_KEY` ni to'ldiring. Yangi kalit yaratish:

```bash
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

Migratsiyalarni bajarib, serverni ishga tushirish:

```bash
python manage.py migrate
python manage.py runserver
```

Sayt <http://127.0.0.1:8000> manzilida ochiladi.

## Ishlab chiqarishga chiqarish

1. `.env` faylida quyidagilarni o'rnatish:

   ```env
   DJANGO_DEBUG=False
   DJANGO_SECRET_KEY=<uzun tasodifiy kalit>
   DJANGO_ALLOWED_HOSTS=varnet.uz,www.varnet.uz
   DJANGO_CSRF_TRUSTED_ORIGINS=https://varnet.uz,https://www.varnet.uz
   ```

2. Statik fayllarni yig'ish:

   ```bash
   python manage.py collectstatic --noinput
   ```

3. Xavfsizlik tekshiruvi:

   ```bash
   python manage.py check --deploy
   ```

4. WSGI server orqali ishga tushirish (masalan Gunicorn + nginx):

   ```bash
   gunicorn varnet.wsgi:application --bind 0.0.0.0:8000
   ```

`DEBUG=False` bo'lganda quyidagilar avtomatik yoqiladi: HTTPS ga
yo'naltirish, HSTS (1 yil, subdomenlar bilan), `Secure` cookie'lar,
manifest bilan siqilgan statik fayllar.

## Serverni yangilash (deploy)

Sayt allaqachon ishlab turgan serverda yangilanishni o'rnatish uchun bitta
buyruq yetarli:

```bash
cd ~/varnet && ./deploy.sh
```

`deploy.sh` ketma-ket bajaradi: sozlama fayllarini zaxiralaydi, GitHub'dan
kodni oladi (`git fetch` + `reset --hard`), sozlamalarni joyiga qaytaradi,
`pip install -r requirements.txt`, `migrate`, `buildmessages`,
`collectstatic` va nihoyat saytni qayta ishga tushiradi.

`varnet/settings.py` va `.env` git'da yo'q, ustiga skript ularni har safar
zaxiralab, pull'dan keyin tiklaydi — serverdagi sozlamalar hech qachon
o'zgarmaydi.

### Birinchi marta (faqat bir marta)

Serverda hozircha `deploy.sh` yo'q va `varnet/settings.py` git tomonidan
kuzatilmoqda. Shuning uchun birinchi yangilanish qo'lda bajariladi —
sozlamani zaxiralab, keyin kodni oling:

```bash
cd ~/varnet
cp varnet/settings.py ~/settings.py.zaxira

git fetch origin
git reset --hard origin/main

cp ~/settings.py.zaxira varnet/settings.py
chmod +x deploy.sh
cp deploy.conf.example deploy.conf   # faqat kerak bo'lsa sozlang

./deploy.sh
```

Shundan keyin `varnet/settings.py` git'dan chiqadi va har safar faqat
`./deploy.sh` yetarli bo'ladi.

`deploy.conf` orqali `PYTHON_BIN` (virtualenv Python'i), `BRANCH`,
`RESTART_CMD` va `SKIP_PIP` ni belgilash mumkin. Hech narsa sozlanmasa,
skript virtualenv'ni o'zi topadi va Passenger uchun `tmp/restart.txt`
faylini yangilaydi.

## Loyiha tuzilishi

```
deploy.sh            Serverga yangilanish o'rnatish skripti
varnet/              Django sozlamalari, URL va WSGI
  settings.example.py  Sozlamalar namunasi (settings.py git'da saqlanmaydi)
main/                Asosiy ilova
  views.py           Sahifa ko'rinishlari va tuzilma PDF generatori
  urls.py            URL marshrutlari
  templatetags/      Shablon filtrlari (til bayroqlari)
  management/commands/
    buildmessages.py Tarjima kataloglarini yig'uvchi buyruq
  templates/main/    Sahifa shablonlari
    base.html        Umumiy karkas (navigatsiya, footer, SEO meta)
    includes/
      page_subheader.html   Barcha ichki sahifalar uchun yagona subheader
locale/
  translations/      Tarjimalar manbasi (til bo'yicha JSON lug'atlar)
  msgids.json        Shablonlardan ajratilgan matnlar
  notranslate.json   Ataylab tarjima qilinmaydigan matnlar
  <til>/LC_MESSAGES/ Yaratilgan .po va .mo fayllari
static/
  css/style.css      Saytning barcha uslublari
  js/main.js         Barcha interaktiv qismlar (modulli, xavfsiz tekshiruvlar bilan)
  images/            Rasmlar (veb uchun optimallashtirilgan)
```

### Yangi sahifa qo'shish

1. `main/views.py` ga ko'rinish funksiyasini qo'shing.
2. `main/urls.py` ga marshrut qo'shing.
3. `main/templates/main/` ichida shablon yarating va subheader'ni ulang:

   ```django
   {% include 'main/includes/page_subheader.html' with
      image='images/subheader/misol-hero.jpg'
      badge_icon='fa-flask' badge='Bo‘lim nomi'
      title='Sahifa <em>sarlavhasi</em>'
      desc='Qisqa tavsif.' crumb='Sahifa' %}
   ```

4. `base.html` navigatsiyasiga havola qo'shing.

## Ko'p tillilik (i18n)

Sayt to'rt tilda ishlaydi: **o'zbek** (asosiy), **rus**, **ingliz**, **turk**.
Tarjima faqat o'zgarmas interfeys matnlariga tegishli — menyular, sarlavhalar,
tugmalar, forma yorliqlari va bo'lim nomlari. Yangilik va e'lon matnlari,
ism-familiyalar hamda rasmiy hujjat nomlari o'zbek tilida qoladi
(ular `locale/notranslate.json` ro'yxatida).

URL manzillari: o'zbek tili prefikssiz (`/aloqa/`), qolgan tillar prefiks bilan
(`/ru/aloqa/`, `/en/aloqa/`, `/tr/aloqa/`). Tanlangan til bir yil davomida
cookie'da saqlanadi.

### Tarjimalarni tahrirlash

GNU gettext (`xgettext`, `msgfmt`) o'rnatilishi shart emas — `.po` va `.mo`
fayllari `polib` yordamida yaratiladi.

1. Shablonda matnni belgilang:

   ```django
   {% load i18n %}
   {% translate "Yangi yorliq" %}

   {# HTML saqlanishi kerak bo'lsa: #}
   {% blocktranslate %}Universitet <em>tuzilmasi</em>{% endblocktranslate %}
   ```

2. Tarjimani mos JSON faylga qo'shing, masalan `locale/translations/ru/A_base.json`:

   ```json
   { "Yangi yorliq": "Новая метка" }
   ```

   Bir til uchun bir nechta JSON fayl bo'lishi mumkin — ular birlashtiriladi.

3. Katalogni qayta yig'ing:

   ```bash
   python manage.py buildmessages          # .po va .mo fayllarini yozadi
   python manage.py buildmessages --check  # faqat yetishmayotganlarni ko'rsatadi
   ```

4. Serverni qayta ishga tushiring — Django `.mo` fayllarini faqat start vaqtida
   o'qiydi.

Yangi til qo'shish uchun `varnet/settings.py` dagi `LANGUAGES` ro'yxatiga kod
qo'shing, `main/templatetags/varnet_extras.py` da bayroq kodini ko'rsating va
`locale/translations/<til>/` katalogini yarating.

## Xususiyatlar

- Barcha ichki sahifalarda yagona, rasmli subheader dizayni
- To'liq moslashuvchan (responsive) dizayn: 390px dan 1440px+ gacha sinovdan o'tgan
- Mobil qurilmalar uchun off-canvas navigatsiya, akkordeon dropdownlar
- Klaviatura bilan boshqarish, `skip-link`, ARIA atributlari, `prefers-reduced-motion` qo'llab-quvvatlashi
- SEO meta teglar, Open Graph, favicon
- Rasmlar `loading="lazy"` bilan yuklanadi
- To'rt tilli interfeys va ishlaydigan til almashtirgich
