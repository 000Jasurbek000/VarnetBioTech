from django import template
from django.conf import settings

register = template.Library()

# flagcdn.com bayroqlarni davlat kodi bilan beradi, til kodi bilan emas.
LANGUAGE_FLAGS = {
    'uz': 'uz',
    'ru': 'ru',
    'en': 'gb',
    'tr': 'tr',
}


@register.filter
def language_flag(language_code):
    """Til kodini flagcdn uchun davlat kodiga aylantiradi."""
    return LANGUAGE_FLAGS.get(language_code, language_code)


@register.filter
def strip_language_prefix(path):
    """i18n_patterns qo'shgan til prefiksini olib tashlaydi: /ru/aloqa/ -> /aloqa/.

    set_language ko'rinishi manzilni faqat prefiksiz holatda tanib, yangi tilga
    o'girishi mumkin (prefix_default_language=False bo'lgani uchun).
    """
    head, _, tail = path.lstrip('/').partition('/')
    if head in dict(settings.LANGUAGES):
        return '/' + tail
    return path
