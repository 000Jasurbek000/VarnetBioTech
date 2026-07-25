from django import template

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
