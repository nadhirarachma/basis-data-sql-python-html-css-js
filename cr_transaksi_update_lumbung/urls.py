from django.urls import path

from . import views

app_name = 'cr_transaksi_update_lumbung'

urlpatterns = [
    path('list-transaksi-lumbung', views.listTransaksiLumbung, name='list-transaksi-lumbung'),
    path('form-upgrade-lumbung', views.formUpgradeLumbung, name='form-upgrade-lumbung'),
    # path('update-paket-koin', views.updatePaketKoin, name='update-paket-koin'),
]
