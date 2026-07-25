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
    return render(request, 'main/structure.html')


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
            {'yil': '2020 – hozir', 'joy': 'Varnet Biotech University', 'lavozim': 'Rektor'},
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
            {'yil': '2021 – hozir', 'joy': 'Varnet Biotech University', 'lavozim': 'Birinchi prorektor'},
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
            {'yil': '2020 – hozir', 'joy': 'Varnet Biotech University', 'lavozim': 'Prorektor'},
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
            {'yil': '2021 – hozir', 'joy': 'Varnet Biotech University', 'lavozim': 'Prorektor'},
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
            {'yil': '2020 – hozir', 'joy': 'Varnet Biotech University', 'lavozim': 'Prorektor'},
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
        'Varnet Biotexnologiyalar Universiteti tashkiliy tuzilmasi',
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
    row3_labels = [
        'Fakultet / Kafedra 1',
        'Fakultet / Kafedra 2',
        'Fakultet / Kafedra 3',
        'Fakultet / Kafedra 4',
        'Fakultet / Kafedra 5',
    ]

    _draw_connector_row(canvas, center_x, rektor_y, rektor_height, centers, row1_y, line_color)
    _draw_box_row(canvas, x_positions, row1_y, row_box_width, row_box_height, row1_labels, box_style, border_color)

    _draw_connector_row(canvas, centers[2], row1_y, row_box_height, centers, row2_y, line_color, branch_width=220)
    _draw_box_row(canvas, x_positions, row2_y, row_box_width, row_box_height, row2_labels, box_style, border_color)

    _draw_connector_row(canvas, centers[2], row2_y, row_box_height, centers, row3_y, line_color, branch_width=220)
    _draw_box_row(canvas, x_positions, row3_y, row_box_width, row_box_height, row3_labels, box_style, border_color)

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
