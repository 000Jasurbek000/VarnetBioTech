# Varnet Biotexnologiyalar Universiteti — veb-sayt

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

Muhit o'zgaruvchilarini sozlang:

```bash
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

## Loyiha tuzilishi

```
varnet/              Django sozlamalari, URL va WSGI
main/                Asosiy ilova
  views.py           Sahifa ko'rinishlari va tuzilma PDF generatori
  urls.py            URL marshrutlari
  templates/main/    Sahifa shablonlari
    base.html        Umumiy karkas (navigatsiya, footer, SEO meta)
    includes/
      page_subheader.html   Barcha ichki sahifalar uchun yagona subheader
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

## Xususiyatlar

- Barcha ichki sahifalarda yagona, rasmli subheader dizayni
- To'liq moslashuvchan (responsive) dizayn: 390px dan 1440px+ gacha sinovdan o'tgan
- Mobil qurilmalar uchun off-canvas navigatsiya, akkordeon dropdownlar
- Klaviatura bilan boshqarish, `skip-link`, ARIA atributlari, `prefers-reduced-motion` qo'llab-quvvatlashi
- SEO meta teglar, Open Graph, favicon
- Rasmlar `loading="lazy"` bilan yuklanadi
