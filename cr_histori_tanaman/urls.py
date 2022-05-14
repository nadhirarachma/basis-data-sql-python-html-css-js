from django.urls import path

from . import views

app_name = 'cr_histori_tanaman'

urlpatterns = [
    path('list-histori-tanaman', views.listHistoriProduksiTanaman, name='list-histori-tanaman'),
    path('form-produksi-tanaman', views.formProduksiTanaman, name='form-produksi-tanaman'),
    # path('update-paket-koin', views.updatePaketKoin, name='update-paket-koin'),
]
