from django.urls import path

from . import views

app_name = 'cr_histori_penjualan'

urlpatterns = [
    path('list-histori-penjualan', views.list_histori_penjualan, name='list-histori-penjualan'),
    path('detail/<str:id>/', views.view_detail_penjualan, name='detail-penjualan'),
    path('ambil-pesanan/<str:id>/', views.ambil_pesanan, name='ambil-pesanan')
]