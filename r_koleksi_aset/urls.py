from django.urls import path

from . import views

app_name = 'r_koleksi_aset'

urlpatterns = [
    path('list-koleksi-aset', views.listKoleksiAset, name='list-koleksi-aset'),
    path('list-koleksi-aset-dekorasi', views.listKoleksiAsetDekorasi, name='list-koleksi-aset-dekorasi'),
    path('list-koleksi-aset-bibit-tanaman', views.listKoleksiAsetBibitTanaman, name='list-koleksi-aset-bibit-tanaman'),
    path('list-koleksi-aset-kandang', views.listKoleksiAsetKandang, name='list-koleksi-aset-kandang'),
    path('list-koleksi-aset-hewan', views.listKoleksiAsetHewan, name='list-koleksi-aset-hewan'),
    path('list-koleksi-aset-alat-produksi', views.listKoleksiAsetAlatProduksi, name='list-koleksi-aset-alat-produksi'),
    path('list-koleksi-aset-petak-sawah', views.listKoleksiAsetPetakSawah, name='list-koleksi-aset-petak-sawah'),
]