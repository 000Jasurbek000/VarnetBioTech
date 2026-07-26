from io import BytesIO

from django.http import Http404, HttpResponse
from django.shortcuts import render

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


def home(request):
    """Home page view"""
    return render(request, 'main/home.html')


def universitet_haqida(request):
    """About university page view"""
    return render(request, 'main/universitet_haqida.html')


def topshiriladigan_hujjatlar(request):
    """Required documents for admission page"""
    return render(request, 'main/topshiriladigan_hujjatlar.html')


def ilmiy_faoliyat(request):
    """Scientific activity page"""
    return render(request, 'main/ilmiy_faoliyat.html')


def barqaror_rivojlanish(request):
    """Sustainable development page"""
    return render(request, 'main/barqaror_rivojlanish.html')


def moliyaviy_faoliyat(request):
    """Financial activity page"""
    return render(request, 'main/moliyaviy_faoliyat.html')


def sport_va_hordiq(request):
    """Sports and leisure page"""
    return render(request, 'main/sport_va_hordiq.html')


def bakalavr_qabuli(request):
    """Bachelor admissions page"""
    return render(request, 'main/bakalavr_qabuli.html')


def magistr_qabuli(request):
    """Master admissions page"""
    return render(request, 'main/magistr_qabuli.html')


def kvota_va_ballar(request):
    """Quota and scores page"""
    return render(request, 'main/kvota_va_ballar.html')


def malaka_oshirish(request):
    """Professional development / training page"""
    return render(request, 'main/malaka_oshirish.html')


def ekofaol_talabalar(request):
    """Eco-active students page"""
    return render(request, 'main/ekofaol_talabalar.html')


def structure(request):
    """University structure page view"""
    return render(request, 'main/structure.html', {'fakultetlar': FAKULTETLAR_DATA.values()})


def aloqa(request):
    """Contact page view"""
    return render(request, 'main/aloqa.html')


def yangiliklar(request):
    """News page view"""
    return render(request, 'main/yangiliklar.html')


def yangilik_detail(request, pk):
    """News detail page view"""
    return render(request, 'main/yangilik_detail.html', {'pk': pk})


def elonlar(request):
    """Announcements page view"""
    return render(request, 'main/elonlar.html')


def elon_detail(request, pk):
    """Announcement detail page view"""
    return render(request, 'main/elon_detail.html', {'pk': pk})


def normativ_hujjatlar(request):
    """Normative documents page"""
    return render(request, 'main/normativ_hujjatlar.html')


def hujjat_topshirish(request):
    """Document submission page view"""
    return render(request, 'main/hujjat_topshirish.html')


def rahbariyat(request):
    """Leadership page view"""
    return render(request, 'main/rahbariyat.html')


RAHBARIYAT_DATA = {
    1: {
        'id': 1,
        'ism': 'Xamidov Obidjon Xafizovich',
        'lavozim': 'Rektor',
        'ilmiy_daraja': 'Iqtisod fanlari doktori, professor',
        'manzil': 'Buxoro shahri, M.Iqbol ko\'chasi 11 uy',
        'email': 'rektor@varnet.uz',
        'qabulvaqti': 'Chorshanba 15:00–17:00, Juma 15:00–17:00',
        'rasm': 'https://picsum.photos/seed/rektor9/300/360',
        'orcid': '',
        'lavozim_vazifalari': [
            'Universitetning ilmiy, ta\'lim va tarbiya sohasidagi faoliyatini boshqarish;',
            'Davlat ta\'lim standartlari asosida o\'quv, ilmiy va tarbiya ishlarini tashkil etish;',
            'Universitetning moliyaviy-xo\'jalik faoliyatini tashkil etish;',
            'Kadrlar siyosatini belgilash va amalga oshirish;',
            'Xalqaro hamkorlik, fan va texnologiyalar rivojini ta\'minlash;',
            'Ta\'lim sifatini nazorat qilish va baholash tizimini joriy etish;',
            'Universitet kollegial boshqaruv organlarining qarorlarini bajarish;',
        ],
        'mehnat_faoliyati': [
            {'yil': '2020 – hozir', 'joy': 'Varnet International Biotechnology University', 'lavozim': 'Rektor'},
            {'yil': '2015 – 2020', 'joy': 'Buxoro davlat universiteti', 'lavozim': 'Prorektor'},
            {'yil': '2010 – 2015', 'joy': 'Buxoro davlat universiteti', 'lavozim': 'Iqtisodiyot kafedrasi mudiri'},
        ],
        'malaka_oshirish': [
            {'yil': '2022', 'joy': 'Rossiya Federatsiyasi, Moskva', 'mavzu': 'Oliy ta\'lim menejment'},
            {'yil': '2019', 'joy': 'Germaniya, Berlin', 'mavzu': 'Zamonaviy ta\'lim texnologiyalari'},
        ],
        'fanlar': [],
        'ilmiy_faoliyat': [
            'Ilmiy maqolalar soni: 45+',
            'Monografiyalar: 3 ta',
            'Patent va ixtirolar: 2 ta',
        ],
    },
    2: {
        'id': 2,
        'ism': 'Qodirov Sherzod Baxtiyorovich',
        'lavozim': 'Yoshlar masalalari va ma\'naviy-ma\'rifiy ishlar bo\'yicha birinchi prorektor',
        'ilmiy_daraja': 'Pedagogika fanlari nomzodi, dotsent',
        'manzil': 'Buxoro shahri, M.Iqbol ko\'chasi 11 uy',
        'email': 'qodirov@varnet.uz',
        'qabulvaqti': 'Seshanba, Payshanba 14:00–16:00',
        'rasm': 'https://picsum.photos/seed/pror1b/300/360',
        'orcid': '',
        'lavozim_vazifalari': [
            'O\'zbekiston Respublikasi qonunlari, Prezident farmonlari va farmoyishlarini amalga oshirishni tashkil etish;',
            'Davlat ta\'lim standartlari asosida ma\'naviy-tarbiya ishlarini tashkil etish va malakali kadrlar tayyorlashni ta\'minlash;',
            'Talaba-yoshlar ongiga milliy g\'oyani singdirish, ma\'naviy-axloqiy tarbiya ishlarini olib borishning amaliy mexanizmlarini shakllantirish;',
            'Ma\'naviy-ma\'rifiy jarayonni boshqarishni takomillashtirib borish;',
            'Ma\'naviy-ma\'rifiy ishlarning joriy va istiqbolli rejalarini ishlab chiqish hamda ularning qat\'iy amalga oshirilishini nazorat qilish;',
            'Respublika, viloyat va shahar miqyosida bo\'ladigan tadbirlarda professor-o\'qituvchilar va talabalarning faol ishtirokini ta\'minlash;',
            'Talabalarning bo\'sh vaqtini mazmunli o\'tkazishni tashkil qilish;',
        ],
        'mehnat_faoliyati': [
            {'yil': '2021 – hozir', 'joy': 'Varnet International Biotechnology University', 'lavozim': 'Birinchi prorektor'},
            {'yil': '2016 – 2021', 'joy': 'Buxoro davlat universiteti', 'lavozim': 'Dekan'},
            {'yil': '2012 – 2016', 'joy': 'Buxoro davlat universiteti', 'lavozim': 'Katta o\'qituvchi'},
        ],
        'malaka_oshirish': [
            {'yil': '2023', 'joy': 'Toshkent shahri', 'mavzu': 'Yoshlar siyosati va ma\'naviy-ma\'rifiy ishlar'},
            {'yil': '2020', 'joy': 'Rossiya, Sankt-Peterburg', 'mavzu': 'Pedagogik texnologiyalar'},
        ],
        'fanlar': ['Pedagogika', 'Ta\'lim falsafasi'],
        'ilmiy_faoliyat': [
            'Ilmiy maqolalar soni: 28+',
            'Monografiyalar: 1 ta',
        ],
    },
    3: {
        'id': 3,
        'ism': 'Toshmatov Otabek Nematovich',
        'lavozim': 'O\'quv ishlari bo\'yicha prorektor',
        'ilmiy_daraja': 'Fizika-matematika fanlari nomzodi',
        'manzil': 'Buxoro shahri, M.Iqbol ko\'chasi 11 uy',
        'email': 'toshmatov@varnet.uz',
        'qabulvaqti': 'Dushanba, Chorshanba 14:00–16:00',
        'rasm': 'https://picsum.photos/seed/pror2b/300/360',
        'orcid': '',
        'lavozim_vazifalari': [
            'O\'quv jarayonini tashkil etish va nazorat qilish;',
            'Yangi o\'quv dasturlari va rejalarini ishlab chiqish;',
            'Ta\'lim sifatini ta\'minlash va baholash tizimini joriy etish;',
            'O\'quv-uslubiy ishlarni muvofiqlashtirilishini ta\'minlash;',
            'Yangi ta\'lim texnologiyalarini joriy etish;',
        ],
        'mehnat_faoliyati': [
            {'yil': '2020 – hozir', 'joy': 'Varnet International Biotechnology University', 'lavozim': 'Prorektor'},
            {'yil': '2015 – 2020', 'joy': 'Buxoro davlat universiteti', 'lavozim': 'Kafedra mudiri'},
        ],
        'malaka_oshirish': [
            {'yil': '2022', 'joy': 'Toshkent', 'mavzu': 'Zamonaviy o\'quv texnologiyalari'},
        ],
        'fanlar': ['Matematika', 'Fizika'],
        'ilmiy_faoliyat': ['Ilmiy maqolalar soni: 32+', 'Monografiyalar: 2 ta'],
    },
    4: {
        'id': 4,
        'ism': 'Yusupova Nilufar Akbarovna',
        'lavozim': 'Ilmiy ishlar va innovatsiyalar bo\'yicha prorektor',
        'ilmiy_daraja': 'Biologiya fanlari doktori',
        'manzil': 'Buxoro shahri, M.Iqbol ko\'chasi 11 uy',
        'email': 'yusupova@varnet.uz',
        'qabulvaqti': 'Seshanba, Juma 13:00–15:00',
        'rasm': 'https://picsum.photos/seed/pror3g/300/360',
        'orcid': '',
        'lavozim_vazifalari': [
            'Ilmiy tadqiqot ishlarini tashkil etish va muvofiqlashtirish;',
            'Ilmiy hamkorlik va innovatsiya loyihalarini amalga oshirish;',
            'Ilmiy nashrlar va monografiyalar nashr etilishini ta\'minlash;',
            'Doktorantura va magistratura qabuli va faoliyatini nazorat qilish;',
            'Xalqaro ilmiy anjumanlar va seminarlarda ishtirok etish;',
        ],
        'mehnat_faoliyati': [
            {'yil': '2021 – hozir', 'joy': 'Varnet International Biotechnology University', 'lavozim': 'Prorektor'},
            {'yil': '2014 – 2021', 'joy': 'Biologiya instituti', 'lavozim': 'Katta ilmiy xodim'},
        ],
        'malaka_oshirish': [
            {'yil': '2021', 'joy': 'Germaniya', 'mavzu': 'Biotexnologiya va innovatsiyalar'},
        ],
        'fanlar': ['Biologiya', 'Biotexnologiya'],
        'ilmiy_faoliyat': ['Ilmiy maqolalar soni: 56+', 'Monografiyalar: 4 ta', 'Patentlar: 5 ta'],
    },
    5: {
        'id': 5,
        'ism': 'Mirzayev Dilshod Sobirovich',
        'lavozim': 'Moliya va iqtisod ishlari bo\'yicha prorektor',
        'ilmiy_daraja': 'Iqtisod fanlari nomzodi',
        'manzil': 'Buxoro shahri, M.Iqbol ko\'chasi 11 uy',
        'email': 'mirzayev@varnet.uz',
        'qabulvaqti': 'Dushanba, Payshanba 15:00–17:00',
        'rasm': 'https://picsum.photos/seed/pror4b/300/360',
        'orcid': '',
        'lavozim_vazifalari': [
            'Universitetning moliyaviy rejasini tuzish va nazorat qilish;',
            'Byudjet mablag\'larini maqsadli va tejamkor sarflanishini ta\'minlash;',
            'Iqtisodiy tahlil va hisobot ishlarini amalga oshirish;',
            'Moddiy-texnik ta\'minot va xo\'jalik masalalarini hal etish;',
        ],
        'mehnat_faoliyati': [
            {'yil': '2020 – hozir', 'joy': 'Varnet International Biotechnology University', 'lavozim': 'Prorektor'},
            {'yil': '2013 – 2020', 'joy': 'Moliya vazirligi', 'lavozim': 'Bosh mutaxassis'},
        ],
        'malaka_oshirish': [
            {'yil': '2022', 'joy': 'Toshkent', 'mavzu': 'Oliy ta\'lim iqtisodiyoti'},
        ],
        'fanlar': ['Moliya', 'Iqtisodiyot'],
        'ilmiy_faoliyat': ['Ilmiy maqolalar soni: 18+'],
    },
}


def rahbariyat_detail(request, pk):
    """Leadership detail page view"""
    person = RAHBARIYAT_DATA.get(pk)
    if not person:
        raise Http404("Rahbar topilmadi")
    return render(request, 'main/rahbariyat_detail.html', {'person': person})


FAKULTETLAR_DATA = {
    1: {
        'id': 1,
        'nom': 'Biotexnologiya fakulteti',
        'qisqa_nom': 'Biotexnologiya',
        'icon': 'fa-dna',
        'rasm': 'images/fakultet/biotexnologiya.jpg',
        'tavsif': 'Zamonaviy biologik texnologiyalar, genetika va molekulyar biologiya sohasida '
                  'chuqur nazariy bilim hamda amaliy ko\'nikma beradi.',
        'tashkil_yili': '2018',
        'yonalishlar_soni': 12,
        'talabalar_soni': 1240,
        'oqituvchilar_soni': 78,
        'laboratoriyalar_soni': 3,
        'email': 'biotex@varnet.uz',
        'telefon': '+998 95 260-11-21',
        'manzil': '1-o\'quv binosi, 2-qavat',
        'dekan': {
            'ism': 'Rahmonov Jasur Alisherovich',
            'lavozim': 'Fakultet dekani',
            'ilmiy_daraja': 'Biologiya fanlari doktori, professor',
            'email': 'j.rahmonov@varnet.uz',
            'qabul_vaqti': 'Dushanba, Chorshanba 14:00–16:00',
            'rasm': '',
        },
        'tarix': [
            'Fakultet universitet tashkil etilgan 2018-yilda birinchilardan bo\'lib faoliyat '
            'boshlagan va bugungi kunda universitetning yetakchi o\'quv-ilmiy bo\'linmasi hisoblanadi.',
            'Fakultet faoliyati sanoat, oziq-ovqat va tibbiy biotexnologiya sohalari uchun yuqori '
            'malakali mutaxassislar tayyorlashga qaratilgan. O\'quv jarayoni xalqaro ta\'lim '
            'dasturlari asosida tashkil etilgan bo\'lib, talabalar birinchi kursdanoq ilmiy '
            'laboratoriyalarda amaliy tadqiqot ishlarida ishtirok etadilar.',
        ],
        'kafedralar': [
            {'nom': 'Sanoat biotexnologiyasi kafedrasi', 'mudir': 'Yo\'ldoshev Aziz Nematovich'},
            {'nom': 'Molekulyar biologiya va genetika kafedrasi', 'mudir': 'Tursunova Zilola Baxodirovna'},
            {'nom': 'Mikrobiologiya va biokimyo kafedrasi', 'mudir': 'Qosimov Ulug\'bek Rustamovich'},
            {'nom': 'Oziq-ovqat biotexnologiyasi kafedrasi', 'mudir': 'Ashurova Dilnoza Sobirovna'},
        ],
        'bakalavr': [
            'Biotexnologiya (tarmoqlar bo\'yicha)',
            'Sanoat biotexnologiyasi',
            'Oziq-ovqat biotexnologiyasi',
            'Molekulyar biologiya',
        ],
        'magistratura': [
            'Sanoat biotexnologiyasi',
            'Molekulyar biotexnologiya va gen muhandisligi',
        ],
        'laboratoriyalar': [
            'Fermentatsiya va bioreaktorlar laboratoriyasi',
            'Molekulyar genetika laboratoriyasi',
            'Mikrobiologik tahlil laboratoriyasi',
        ],
        'hamkorlar_mahalliy': [
            'O\'zbekiston Milliy universiteti',
            'O\'zR FA Genetika va o\'simliklar eksperimental biologiyasi instituti',
            'O\'zR FA Mikrobiologiya instituti',
            'Buxoro muhandislik-texnologiya instituti',
        ],
        'hamkorlar_xalqaro': [
            'Wageningen universiteti (Niderlandiya)',
            'Seul milliy universiteti (Janubiy Koreya)',
            'Ankara universiteti (Turkiya)',
        ],
        'yutuqlar': [
            'So\'nggi uch yilda fakultet professor-o\'qituvchilari tomonidan 2 ta darslik, '
            '4 ta o\'quv qo\'llanma va 60 dan ortiq ilmiy maqola chop etildi, shulardan 14 tasi '
            'impakt-faktorga ega xorijiy jurnallarda nashr qilindi.',
            'Fakultet talabalari respublika fan olimpiadalari va startap tanlovlarida muntazam '
            'sovrinli o\'rinlarni egallab kelmoqda.',
        ],
    },
    2: {
        'id': 2,
        'nom': 'Ekologiya va atrof-muhit fakulteti',
        'qisqa_nom': 'Ekologiya',
        'icon': 'fa-leaf',
        'rasm': 'images/fakultet/ekologiya.jpg',
        'tavsif': 'Tabiatni muhofaza qilish, ekologik monitoring va barqaror rivojlanish '
                  'yo\'nalishlarida mutaxassislar tayyorlaydi.',
        'tashkil_yili': '2018',
        'yonalishlar_soni': 8,
        'talabalar_soni': 720,
        'oqituvchilar_soni': 42,
        'laboratoriyalar_soni': 2,
        'email': 'ekologiya@varnet.uz',
        'telefon': '+998 95 260-11-22',
        'manzil': '2-o\'quv binosi, 1-qavat',
        'dekan': {
            'ism': 'Ergasheva Nodira Baxtiyorovna',
            'lavozim': 'Fakultet dekani',
            'ilmiy_daraja': 'Biologiya fanlari nomzodi, dotsent',
            'email': 'n.ergasheva@varnet.uz',
            'qabul_vaqti': 'Seshanba, Payshanba 14:00–16:00',
            'rasm': '',
        },
        'tarix': [
            'Fakultet 2018-yilda universitet tarkibida tashkil etilgan bo\'lib, mintaqada '
            'ekologik xavfsizlik va suv resurslarini boshqarish muammolarini hal etishga '
            'yo\'naltirilgan kadrlar tayyorlaydi.',
            'Fakultet Barqaror rivojlanish maqsadlari (BRM) doirasidagi universitet strategiyasini '
            'amalga oshirishda yetakchi bo\'linma hisoblanadi va "Yashil universitet" tashabbusini '
            'muvofiqlashtiradi.',
        ],
        'kafedralar': [
            {'nom': 'Ekologiya va atrof-muhit muhofazasi kafedrasi', 'mudir': 'Xolmurodov Sanjar Ilhomovich'},
            {'nom': 'Ekologik monitoring kafedrasi', 'mudir': 'Rasulova Shahnoza Anvarovna'},
            {'nom': 'Suv resurslari va tuproqshunoslik kafedrasi', 'mudir': 'Bekmurodov Otabek Zafarovich'},
        ],
        'bakalavr': [
            'Ekologiya va atrof-muhit muhofazasi',
            'Ekologik monitoring va ekspertiza',
            'Suv resurslarini boshqarish',
        ],
        'magistratura': [
            'Atrof-muhit muhofazasi va barqaror rivojlanish',
            'Ekologik xavfsizlik',
        ],
        'laboratoriyalar': [
            'Atrof-muhit tahlili laboratoriyasi',
            'Suv va tuproq sifati laboratoriyasi',
        ],
        'hamkorlar_mahalliy': [
            'Ekologiya, atrof-muhitni muhofaza qilish va iqlim o\'zgarishi vazirligi',
            'O\'zgidromet markazi',
            'Buxoro viloyati ekologiya boshqarmasi',
        ],
        'hamkorlar_xalqaro': [
            'Bern universiteti (Shveytsariya)',
            'Uppsala universiteti (Shvetsiya)',
            'Qozog\'iston milliy agrar universiteti (Qozog\'iston)',
        ],
        'yutuqlar': [
            'Fakultet tashabbusi bilan universitet hududida quyosh panellari o\'rnatildi va '
            'yog\'in suvlarini qayta ishlatish tizimi joriy etildi.',
            'Talabalarning "Ekofaol talabalar" harakati har yili mintaqada 5 mingdan ortiq '
            'ko\'chat ekish aksiyalarini tashkil qiladi.',
        ],
    },
    3: {
        'id': 3,
        'nom': 'Innovatsion texnologiyalar fakulteti',
        'qisqa_nom': 'Innovatsion texnologiyalar',
        'icon': 'fa-microchip',
        'rasm': 'images/fakultet/innovatsion.jpg',
        'tavsif': 'Bioinformatika, sun\'iy intellekt va raqamli texnologiyalarni biologiya '
                  'bilan bog\'laydigan zamonaviy yo\'nalishlar.',
        'tashkil_yili': '2019',
        'yonalishlar_soni': 15,
        'talabalar_soni': 1150,
        'oqituvchilar_soni': 65,
        'laboratoriyalar_soni': 2,
        'email': 'innovatsiya@varnet.uz',
        'telefon': '+998 95 260-11-23',
        'manzil': '3-o\'quv binosi, 3-qavat',
        'dekan': {
            'ism': 'Umarov Sardor G\'ayratovich',
            'lavozim': 'Fakultet dekani',
            'ilmiy_daraja': 'Texnika fanlari nomzodi, dotsent',
            'email': 's.umarov@varnet.uz',
            'qabul_vaqti': 'Dushanba, Juma 15:00–17:00',
            'rasm': '',
        },
        'tarix': [
            'Fakultet 2019-yilda biologiya va axborot texnologiyalari kesishmasidagi yangi '
            'kasblarga bo\'lgan ehtiyojni qondirish maqsadida tashkil etilgan.',
            'Bugungi kunda fakultet universitetning barcha ilmiy bo\'linmalari uchun ma\'lumotlarni '
            'tahlil qilish, modellashtirish va raqamli infratuzilma bo\'yicha xizmat ko\'rsatadi.',
        ],
        'kafedralar': [
            {'nom': 'Bioinformatika kafedrasi', 'mudir': 'Nazarov Jahongir Farhodovich'},
            {'nom': 'Sun\'iy intellekt va ma\'lumotlar tahlili kafedrasi', 'mudir': 'Sattorova Kamola Erkinovna'},
            {'nom': 'Raqamli texnologiyalar kafedrasi', 'mudir': 'Xudoyberdiyev Rustam Olimovich'},
            {'nom': 'Biotexnik tizimlar kafedrasi', 'mudir': 'Mahmudova Sevara Qahramonovna'},
        ],
        'bakalavr': [
            'Bioinformatika',
            'Kompyuter injiniringi (biotexnik tizimlar)',
            'Axborot tizimlari va texnologiyalari',
            'Sun\'iy intellekt',
        ],
        'magistratura': [
            'Bioinformatika va hisoblash biologiyasi',
            'Ma\'lumotlar fani',
        ],
        'laboratoriyalar': [
            'Hisoblash biologiyasi laboratoriyasi',
            'Sun\'iy intellekt va robototexnika laboratoriyasi',
        ],
        'hamkorlar_mahalliy': [
            'Muhammad al-Xorazmiy nomidagi TATU',
            'IT Park O\'zbekiston',
            'O\'zR FA Kibernetika instituti',
        ],
        'hamkorlar_xalqaro': [
            'Tallinn texnika universiteti (Estoniya)',
            'Istanbul texnika universiteti (Turkiya)',
            'Varshava texnologiya universiteti (Polsha)',
        ],
        'yutuqlar': [
            'Fakultet talabalari jamoasi xalqaro hackathon va dasturlash musobaqalarida '
            'muntazam ishtirok etib, so\'nggi ikki yilda 6 ta sovrinli o\'rinni qo\'lga kiritdi.',
            'Fakultetda universitet ilmiy ma\'lumotlar omborini boshqaruvchi raqamli platforma '
            'ishlab chiqildi va amaliyotga joriy etildi.',
        ],
    },
    4: {
        'id': 4,
        'nom': 'Kimyo va farmatsevtika fakulteti',
        'qisqa_nom': 'Kimyo va farmatsevtika',
        'icon': 'fa-flask',
        'rasm': 'images/fakultet/farmatsevtika.jpg',
        'tavsif': 'Organik kimyo, dori vositalari ishlab chiqarish va farmatsevtik '
                  'texnologiyalar yo\'nalishlarida ta\'lim beradi.',
        'tashkil_yili': '2018',
        'yonalishlar_soni': 10,
        'talabalar_soni': 890,
        'oqituvchilar_soni': 51,
        'laboratoriyalar_soni': 2,
        'email': 'farmatsevtika@varnet.uz',
        'telefon': '+998 95 260-11-24',
        'manzil': '2-o\'quv binosi, 3-qavat',
        'dekan': {
            'ism': 'Saidova Gulnora Rustamovna',
            'lavozim': 'Fakultet dekani',
            'ilmiy_daraja': 'Kimyo fanlari doktori, professor',
            'email': 'g.saidova@varnet.uz',
            'qabul_vaqti': 'Chorshanba, Juma 14:00–16:00',
            'rasm': '',
        },
        'tarix': [
            'Fakultet universitet tashkil etilgan yildan buyon faoliyat yuritadi va farmatsevtika '
            'sanoati uchun kimyogar-texnolog kadrlar tayyorlaydi.',
            'O\'quv jarayonida GMP (Good Manufacturing Practice) standartlariga asoslangan amaliy '
            'mashg\'ulotlarga alohida e\'tibor qaratiladi.',
        ],
        'kafedralar': [
            {'nom': 'Organik va analitik kimyo kafedrasi', 'mudir': 'Jo\'rayev Alisher Baxtiyorovich'},
            {'nom': 'Farmatsevtika texnologiyasi kafedrasi', 'mudir': 'Islomova Nigora Davronovna'},
            {'nom': 'Farmakognoziya kafedrasi', 'mudir': 'Karimov Doniyor Shuhratovich'},
        ],
        'bakalavr': [
            'Farmatsevtika (tayyor dori vositalari texnologiyasi)',
            'Kimyoviy texnologiya',
            'Analitik kimyo',
        ],
        'magistratura': [
            'Farmatsevtika biotexnologiyasi',
            'Dori vositalari standartlashtirish va sifat nazorati',
        ],
        'laboratoriyalar': [
            'Analitik kimyo laboratoriyasi',
            'Farmatsevtik texnologiya laboratoriyasi',
        ],
        'hamkorlar_mahalliy': [
            'Toshkent farmatsevtika instituti',
            'O\'zbekiston farmatsevtika sanoati assotsiatsiyasi',
            'O\'zR FA O\'simlik moddalari kimyosi instituti',
        ],
        'hamkorlar_xalqaro': [
            'Hacettepe universiteti (Turkiya)',
            'Kaunas tibbiyot universiteti (Litva)',
            'Qozon federal universiteti (Rossiya)',
        ],
        'yutuqlar': [
            'Fakultet olimlari mahalliy o\'simlik xomashyosi asosida biologik faol qo\'shimchalar '
            'ishlab chiqish bo\'yicha 3 ta patent oldi.',
            'Fakultet farmatsevtika korxonalari bilan hamkorlikda talabalarni ishlab chiqarish '
            'amaliyoti bilan to\'liq ta\'minlaydi.',
        ],
    },
    5: {
        'id': 5,
        'nom': 'Agrobiotexnologiya fakulteti',
        'qisqa_nom': 'Agrobiotexnologiya',
        'icon': 'fa-seedling',
        'rasm': 'images/fakultet/agrobiotexnologiya.jpg',
        'tavsif': 'Qishloq xo\'jaligi biotexnologiyasi, gen muhandisligi va zamonaviy '
                  'o\'simlik seleksiyasi yo\'nalishlari.',
        'tashkil_yili': '2019',
        'yonalishlar_soni': 7,
        'talabalar_soni': 610,
        'oqituvchilar_soni': 38,
        'laboratoriyalar_soni': 1,
        'email': 'agro@varnet.uz',
        'telefon': '+998 95 260-11-25',
        'manzil': '4-o\'quv binosi, 1-qavat',
        'dekan': {
            'ism': 'Norqulov Bekzod Shavkatovich',
            'lavozim': 'Fakultet dekani',
            'ilmiy_daraja': 'Qishloq xo\'jaligi fanlari nomzodi, dotsent',
            'email': 'b.norqulov@varnet.uz',
            'qabul_vaqti': 'Seshanba, Juma 13:00–15:00',
            'rasm': '',
        },
        'tarix': [
            'Fakultet 2019-yilda mintaqa qishloq xo\'jaligini zamonaviy biotexnologiya yutuqlari '
            'bilan ta\'minlash maqsadida tashkil etilgan.',
            'Universitetning tajriba maydoni va issiqxona majmuasi fakultet ixtiyorida bo\'lib, '
            'talabalar sho\'r va qurg\'oqchilikka chidamli navlarni sinovdan o\'tkazishda '
            'bevosita ishtirok etadilar.',
        ],
        'kafedralar': [
            {'nom': 'O\'simliklar biotexnologiyasi va seleksiya kafedrasi', 'mudir': 'Ochilov Sherzod Tolibovich'},
            {'nom': 'Agrokimyo va tuproqshunoslik kafedrasi', 'mudir': 'Yusupova Dilbar Nurullayevna'},
            {'nom': 'Chorvachilik biotexnologiyasi kafedrasi', 'mudir': 'Toshpo\'latov Jamshid Baxtiyorovich'},
        ],
        'bakalavr': [
            'Agrobiotexnologiya',
            'O\'simliklarni himoya qilish va karantin',
            'Tuproqshunoslik va agrokimyo',
        ],
        'magistratura': [
            'O\'simliklar biotexnologiyasi va seleksiya',
            'Chorvachilik biotexnologiyasi',
        ],
        'laboratoriyalar': [
            'O\'simlik to\'qimalari kulturasi laboratoriyasi',
        ],
        'hamkorlar_mahalliy': [
            'Toshkent davlat agrar universiteti',
            'O\'simlikshunoslik ilmiy-tadqiqot instituti',
            'Buxoro viloyati fermerlar kengashi',
        ],
        'hamkorlar_xalqaro': [
            'ICARDA xalqaro markazi',
            'Chexiya hayot fanlari universiteti (Chexiya)',
            'Selchuk universiteti (Turkiya)',
        ],
        'yutuqlar': [
            'Fakultet olimlari sho\'rlangan tuproqlarda o\'stirishga mo\'ljallangan ikkita '
            'bug\'doy navini sinovdan o\'tkazmoqda.',
            'Tajriba issiqxonasida to\'qima kulturasi usulida ko\'paytirilgan ko\'chatlar '
            'mintaqa fermer xo\'jaliklariga yetkazib berilmoqda.',
        ],
    },
    6: {
        'id': 6,
        'nom': 'Tibbiy biotexnologiya fakulteti',
        'qisqa_nom': 'Tibbiy biotexnologiya',
        'icon': 'fa-heartbeat',
        'rasm': 'images/fakultet/tibbiy.jpg',
        'tavsif': 'Tibbiyot maqsadlarida biologik texnologiyalardan foydalanish, tashxis '
                  'va davolash tizimlari.',
        'tashkil_yili': '2020',
        'yonalishlar_soni': 9,
        'talabalar_soni': 810,
        'oqituvchilar_soni': 46,
        'laboratoriyalar_soni': 2,
        'email': 'tibbiy@varnet.uz',
        'telefon': '+998 95 260-11-26',
        'manzil': '1-o\'quv binosi, 4-qavat',
        'dekan': {
            'ism': 'Aliyeva Malika Farhodovna',
            'lavozim': 'Fakultet dekani',
            'ilmiy_daraja': 'Tibbiyot fanlari doktori, professor',
            'email': 'm.aliyeva@varnet.uz',
            'qabul_vaqti': 'Dushanba, Payshanba 14:00–16:00',
            'rasm': '',
        },
        'tarix': [
            'Fakultet 2020-yilda tibbiy diagnostika va biopreparatlar sohasidagi kadrlarga '
            'bo\'lgan ehtiyojni qondirish maqsadida ochilgan.',
            'Fakultet mintaqadagi klinika va diagnostika markazlari bilan hamkorlikda '
            'talabalarning klinik amaliyotini tashkil etadi.',
        ],
        'kafedralar': [
            {'nom': 'Tibbiy biologiya kafedrasi', 'mudir': 'Sobirov Nodirbek Ilhomjonovich'},
            {'nom': 'Immunologiya va biotexnologiya kafedrasi', 'mudir': 'Qurbonova Ziyoda Akmalovna'},
            {'nom': 'Klinik laboratoriya diagnostikasi kafedrasi', 'mudir': 'Hamroyev Bunyod Sanjarovich'},
        ],
        'bakalavr': [
            'Tibbiy biotexnologiya',
            'Klinik laboratoriya diagnostikasi',
            'Biotibbiyot muhandisligi',
        ],
        'magistratura': [
            'Tibbiy biotexnologiya',
            'Immunobiotexnologiya',
        ],
        'laboratoriyalar': [
            'Hujayra kulturasi laboratoriyasi',
            'Klinik diagnostika laboratoriyasi',
        ],
        'hamkorlar_mahalliy': [
            'Toshkent tibbiyot akademiyasi',
            'Buxoro davlat tibbiyot instituti',
            'Respublika ixtisoslashtirilgan immunologiya markazi',
        ],
        'hamkorlar_xalqaro': [
            'Ege universiteti (Turkiya)',
            'Lyublyana universiteti (Sloveniya)',
            'Seul milliy universiteti (Janubiy Koreya)',
        ],
        'yutuqlar': [
            'Fakultet bazasida tez tashxis test tizimlarini ishlab chiqish bo\'yicha ilmiy '
            'guruh faoliyat yuritmoqda.',
            'Talabalar xalqaro tibbiyot konferensiyalarida ma\'ruzalar bilan qatnashib, '
            'so\'nggi yilda 4 ta ilmiy maqola chop etdi.',
        ],
    },
}


def fakultetlar(request):
    """Faculties overview page"""
    return render(request, 'main/fakultetlar.html', {'fakultetlar': FAKULTETLAR_DATA.values()})


def fakultet_detail(request, pk):
    """Single faculty page"""
    fakultet = FAKULTETLAR_DATA.get(pk)
    if not fakultet:
        raise Http404("Fakultet topilmadi")
    boshqalar = [item for item in FAKULTETLAR_DATA.values() if item['id'] != pk]
    return render(request, 'main/fakultet_detail.html', {'fakultet': fakultet, 'boshqalar': boshqalar})


def download_structure_pdf(request):
    """Download the university structure as a PDF file."""
    buffer = BytesIO()
    pdf = _build_structure_pdf(buffer)
    response = HttpResponse(pdf.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="universitet_tuzilmasi.pdf"'
    return response


def _build_structure_pdf(buffer):
    page_width, page_height = landscape(A3)
    canvas = Canvas(buffer, pagesize=(page_width, page_height))

    background = colors.HexColor('#f0f4f8')
    border_color = colors.HexColor('#b0c8d8')
    line_color = colors.HexColor('#9ab0c0')
    text_color = colors.HexColor('#2c3e50')
    rektor_color = colors.HexColor('#0d2d5e')

    canvas.setFillColor(background)
    canvas.rect(0, 0, page_width, page_height, fill=1, stroke=0)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'StructureTitle',
        parent=styles['Heading1'],
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        fontSize=32,
        leading=38,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=8,
    )
    subtitle_style = ParagraphStyle(
        'StructureSubtitle',
        parent=styles['BodyText'],
        alignment=TA_CENTER,
        fontName='Helvetica',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#999999'),
    )
    box_style = ParagraphStyle(
        'StructureBox',
        parent=styles['BodyText'],
        alignment=TA_CENTER,
        fontName='Helvetica',
        fontSize=13,
        leading=16,
        textColor=text_color,
    )
    rektor_style = ParagraphStyle(
        'StructureRektor',
        parent=styles['BodyText'],
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=19,
        textColor=colors.white,
    )

    title_y = page_height - 60
    _draw_centered_paragraph(canvas, 'Universitet tuzilmasi', title_style, 0, title_y - 16, page_width, 40)
    _draw_centered_paragraph(
        canvas,
        'Varnet Xalqaro Biotexnologiyalar Universiteti tashkiliy tuzilmasi',
        subtitle_style,
        0,
        title_y - 45,
        page_width,
        22,
    )

    center_x = page_width / 2
    rektor_width = 180
    rektor_height = 55
    rektor_y = page_height - 165
    _draw_box(
        canvas,
        center_x - rektor_width / 2,
        rektor_y,
        rektor_width,
        rektor_height,
        'Rektor',
        rektor_style,
        fill_color=rektor_color,
        stroke_color=rektor_color,
        radius=30,
        shadow=True,
    )

    row_box_width = 200
    row_box_height = 90
    chart_left = 50
    chart_width = page_width - 100
    gap = (chart_width - row_box_width * 5) / 4
    x_positions = [chart_left + index * (row_box_width + gap) for index in range(5)]
    centers = [position + row_box_width / 2 for position in x_positions]

    row1_y = rektor_y - 172
    row2_y = row1_y - 172
    row3_y = row2_y - 172

    row1_labels = [
        "Yoshlar masalalari va ma'naviy-ma'rifiy ishlar bo'yicha birinchi prorektor",
        "O'quv ishlari bo'yicha prorektor",
        "Ilmiy ishlar va innovatsiyalar bo'yicha prorektor",
        "Moliya iqtisod ishlari bo'yicha prorektor",
        "Xalqaro hamkorlik bo'yicha prorektor",
    ]
    row2_labels = [
        "Magistratura bo'limi",
        "O'quv-uslubiy bo'lim",
        "Ilmiy tadqiqot bo'limi",
        "Moliya bo'limi",
        "Xalqaro aloqalar bo'limi",
    ]
    # Fakultetlar qatori kengroq — oltita quti sig'ishi uchun alohida hisoblanadi.
    fakultet_labels = [fakultet['nom'] for fakultet in FAKULTETLAR_DATA.values()]
    fakultet_box_width = 165
    fakultet_gap = (chart_width - fakultet_box_width * len(fakultet_labels)) / (len(fakultet_labels) - 1)
    fakultet_x_positions = [
        chart_left + index * (fakultet_box_width + fakultet_gap) for index in range(len(fakultet_labels))
    ]
    fakultet_centers = [position + fakultet_box_width / 2 for position in fakultet_x_positions]
    fakultet_style = ParagraphStyle('StructureFakultet', parent=box_style, fontSize=11, leading=14)

    _draw_connector_row(canvas, center_x, rektor_y, rektor_height, centers, row1_y, line_color)
    _draw_box_row(canvas, x_positions, row1_y, row_box_width, row_box_height, row1_labels, box_style, border_color)

    _draw_connector_row(canvas, centers[2], row1_y, row_box_height, centers, row2_y, line_color, branch_width=220)
    _draw_box_row(canvas, x_positions, row2_y, row_box_width, row_box_height, row2_labels, box_style, border_color)

    _draw_connector_row(
        canvas, centers[2], row2_y, row_box_height, fakultet_centers, row3_y, line_color, branch_width=220
    )
    _draw_box_row(
        canvas,
        fakultet_x_positions,
        row3_y,
        fakultet_box_width,
        row_box_height,
        fakultet_labels,
        fakultet_style,
        border_color,
    )

    canvas.showPage()
    canvas.save()
    buffer.seek(0)
    return buffer


def _draw_centered_paragraph(canvas, text, style, x, y, width, height):
    paragraph = Paragraph(text, style)
    paragraph.wrap(width, height)
    paragraph.drawOn(canvas, x, y)


def _draw_box(canvas, x, y, width, height, text, style, fill_color, stroke_color, radius=8, shadow=False):
    if shadow:
        shadow_offset = 2
        shadow_color = colors.Color(0, 0, 0, alpha=0.07)
        canvas.setFillColor(shadow_color)
        canvas.setStrokeColor(shadow_color)
        for offset in range(1, 9):
            canvas.roundRect(
                x + shadow_offset, 
                y - shadow_offset - offset/4, 
                width, 
                height, 
                radius, 
                fill=1, 
                stroke=0
            )
    
    canvas.setFillColor(fill_color)
    canvas.setStrokeColor(stroke_color)
    canvas.setLineWidth(1.5)
    canvas.roundRect(x, y, width, height, radius, fill=1, stroke=1)

    paragraph = Paragraph(text, style)
    available_width = width - 20
    available_height = height - 15
    paragraph_width, paragraph_height = paragraph.wrap(available_width, available_height)
    paragraph_x = x + (width - paragraph_width) / 2
    paragraph_y = y + (height - paragraph_height) / 2
    paragraph.drawOn(canvas, paragraph_x, paragraph_y)


def _draw_box_row(canvas, x_positions, y, width, height, labels, style, border_color):
    for index, label in enumerate(labels):
        _draw_box(
            canvas,
            x_positions[index],
            y,
            width,
            height,
            label,
            style,
            fill_color=colors.white,
            stroke_color=border_color,
        )


def _draw_connector_row(canvas, source_center_x, source_y, source_height, centers, target_y, line_color, branch_width=None):
    source_bottom = source_y
    vertical_drop = 70
    line_top = source_bottom - vertical_drop
    horizontal_y = line_top - 28
    target_top = target_y + 90

    canvas.setStrokeColor(line_color)
    canvas.setLineWidth(2)
    canvas.line(source_center_x, source_bottom, source_center_x, line_top)

    if branch_width:
        left_x = source_center_x - branch_width / 2
        right_x = source_center_x + branch_width / 2
        canvas.line(left_x, line_top, left_x, target_top)
        canvas.line(right_x, line_top, right_x, target_top)
    
    left_x = min(centers)
    right_x = max(centers)
    canvas.line(left_x, horizontal_y, right_x, horizontal_y)

    for center_x in centers:
        canvas.line(center_x, horizontal_y, center_x, target_top)
