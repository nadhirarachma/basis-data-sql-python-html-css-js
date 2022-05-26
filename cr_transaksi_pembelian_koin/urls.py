from django.urls import path

from . import views

app_name = 'cr_transaksi_pembelian_koin'

urlpatterns = [
    path('list-transaksi-paket-koin', views.listTransaksiPaketKoin, name='list-transaksi-paket-koin'),
    path('form-transaksi-paket-koin/<slug:slug>', views.formPaketKoin, name='form-transaksi-paket-koin'),
    # path('update-paket-koin', views.updatePaketKoin, name='update-paket-koin'),
]
