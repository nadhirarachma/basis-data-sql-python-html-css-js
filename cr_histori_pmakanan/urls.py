from django.urls import path

from . import views

app_name = 'cr_histori_pmakanan'

urlpatterns = [
    path('list-histori-pmakanan', views.listHistori, name='list-produksi'),
    path('buat-histori-pmakanan', views.buatProduksi, name='buat-produksi'),
    ]
