from django.urls import path

from . import views

app_name = 'r_koleksi_aset'

urlpatterns = [
    path('list-koleksi-aset', views.listKoleksiAset, name='list-koleksi-aset'),
]