from django.urls import path

from . import views

app_name = 'crud_aset'

urlpatterns = [
    path('list-aset', views.listAset, name='list-aset'),
    path('list-dekorasi', views.listDekorasi, name='list-dekorasi'),
    path('list-bibit-tanaman', views.listBibitTanaman, name='list-bibit-tanaman'),
    path('list-kandang', views.listKandang, name='list-kandang'),
    path('list-hewan', views.listHewan, name='list-hewan'),
    path('list-alat-produksi', views.listAlatProduksi, name='list-alat-produksi'),
    path('list-petak-sawah', views.listPetakSawah, name='list-petak-sawah'),
    path('buat-aset', views.buatAset, name='buat-aset'),
    path('buat-dekorasi', views.buatDekorasi, name='buat-dekorasi'),
    path('buat-bibit-tanaman', views.buatBibitTanaman, name='buat-bibit-tanaman'),
    path('buat-kandang', views.buatKandang, name='buat-kandang'),
    path('buat-hewan', views.buatHewan, name='buat-hewan'),
    path('buat-alat-produksi', views.buatAlatProduksi, name='buat-alat-produksi'),
    path('buat-petak-sawah', views.buatPetakSawah, name='buat-petak-sawah'),
    path('ubah-dekorasi', views.ubahDekorasi, name='ubah-dekorasi'),
    path('ubah-bibit-tanaman', views.ubahBibitTanaman, name='ubah-bibit-tanaman'),
    path('ubah-kandang', views.ubahKandang, name='ubah-kandang'),
    path('ubah-hewan', views.ubahHewan, name='ubah-hewan'),
    path('ubah-alat-produksi', views.ubahAlatProduksi, name='ubah-alat-produksi'),
    path('ubah-petak-sawah', views.ubahPetakSawah, name='ubah-petak-sawah'),
]