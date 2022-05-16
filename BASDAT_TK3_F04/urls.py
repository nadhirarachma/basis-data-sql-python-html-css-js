"""BASDAT_TK3_F04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django import urls
from cr_histori_hewan.views import list_histori_hewan, produksi_hewan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('crud-produk/', include('crud_produk.urls')),
    path('crud-paket-koin/', include('crud_paket_koin.urls')),
    path('cr-transaksi-pembelian-koin/', include('cr_transaksi_pembelian_koin.urls')),
    path('cr-transaksi-upgrade-lumbung/', include('cr_transaksi_update_lumbung.urls')),
    path('cr-histori-tanaman/', include('cr_histori_tanaman.urls')),
    path('crud-pesanan/', include('crud_pesanan.urls')),
    path('cr-histori-hewan/', include('cr_histori_hewan.urls')),
    path('cr-histori-penjualan/', include('cr_histori_penjualan.urls')),
    path('crud-produksi/', include('crud_produksi.urls')),
    path('cr-histori-pmakanan/', include('cr_histori_pmakanan.urls')),
    path('crud-aset/', include('crud_aset.urls')),
    path('r-koleksi-aset/', include('r_koleksi_aset.urls')),
    path('cr-transaksi-pembelian-aset/', include('cr_transaksi_pembelian_aset.urls')),
]
