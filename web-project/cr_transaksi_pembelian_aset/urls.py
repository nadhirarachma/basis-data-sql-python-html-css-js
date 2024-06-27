from django.urls import path

from . import views

app_name = 'cr_transaksi_pembelian_aset'

urlpatterns = [
    path('list-transaksi-pembelian-aset', views.listTransaksiPembelianAset, name='list-transaksi-pembelian-aset'),
    path('buat-transaksi-pembelian-aset', views.buatTransaksiPembelianAset, name='buat-transaksi-pembelian-aset'),
]