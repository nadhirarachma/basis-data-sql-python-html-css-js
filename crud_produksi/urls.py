from django.urls import path

from . import views

app_name = 'crud_produksi'

urlpatterns = [
    path('list-produksi', views.listProduksi, name='list-produksi'),
    path('buat-produksi', views.buatProduksi, name='buat-produksi'),
    path('detail-produksi/<slug:slug>', views.detailProduksi, name='detail-produksi'),
    path('ubah-produksi/<slug:slug>', views.ubahProduksi, name='ubah-produksi'),
    path('delete-produksi/<slug:slug>', views.deleteProduksi, name='delete-produksi'),
    ]
