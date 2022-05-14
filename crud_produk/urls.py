from django.urls import path

from . import views

app_name = 'crud_produk'

urlpatterns = [
    path('list-produk', views.listProduk, name='list-produk'),
    path('list-produksi', views.listProduksi, name='list-produksi'),
    path('buat-produk', views.buatProduk, name='buat-produk'),
    path('ubah-produk', views.ubahProduk, name='ubah-produk'),
    path('buat-produksi', views.buatProduksi, name='buat-produksi'),
    ]
