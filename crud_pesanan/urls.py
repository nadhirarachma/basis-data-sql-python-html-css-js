from django.urls import path

from . import views

app_name = 'crud_pesanan'

urlpatterns = [
    path('list-histori-pesanan', views.list_histori_pesanan, name='list-histori-pesanan'),
    path('detail/<str:id>/', views.view_detail_pesanan, name='detail-pesanan'),
    path('buat-pesanan', views.buat_pesanan, name='buat-pesanan'),
    path('update/<str:id>/', views.ubah_pesanan, name='update-pesan')
]