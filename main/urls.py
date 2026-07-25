from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('tuzilma/', views.structure, name='structure'),
    path('tuzilma/pdf/', views.download_structure_pdf, name='structure_pdf'),
    path('aloqa/', views.aloqa, name='aloqa'),
    path('yangiliklar/', views.yangiliklar, name='yangiliklar'),
    path('yangiliklar/<int:pk>/', views.yangilik_detail, name='yangilik_detail'),
    path('elonlar/', views.elonlar, name='elonlar'),
    path('elonlar/<int:pk>/', views.elon_detail, name='elon_detail'),
    path('normativ-hujjatlar/', views.normativ_hujjatlar, name='normativ_hujjatlar'),
    path('hujjat-topshirish/', views.hujjat_topshirish, name='hujjat_topshirish'),
    path('rahbariyat/', views.rahbariyat, name='rahbariyat'),
    path('rahbariyat/<int:pk>/', views.rahbariyat_detail, name='rahbariyat_detail'),
    path('universitet-haqida/', views.universitet_haqida, name='universitet_haqida'),
    path('topshiriladigan-hujjatlar/', views.topshiriladigan_hujjatlar, name='topshiriladigan_hujjatlar'),
    path('ilmiy-faoliyat/', views.ilmiy_faoliyat, name='ilmiy_faoliyat'),
    path('barqaror-rivojlanish/', views.barqaror_rivojlanish, name='barqaror_rivojlanish'),
    path('moliyaviy-faoliyat/', views.moliyaviy_faoliyat, name='moliyaviy_faoliyat'),
    path('sport-va-hordiq/', views.sport_va_hordiq, name='sport_va_hordiq'),
    path('bakalavr-qabuli/', views.bakalavr_qabuli, name='bakalavr_qabuli'),
    path('magistr-qabuli/', views.magistr_qabuli, name='magistr_qabuli'),
    path('kvota-va-ballar/', views.kvota_va_ballar, name='kvota_va_ballar'),
    path('malaka-oshirish/', views.malaka_oshirish, name='malaka_oshirish'),
    path('ekofaol-talabalar/', views.ekofaol_talabalar, name='ekofaol_talabalar'),
]
