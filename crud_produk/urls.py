from django.urls import path

from . import views

app_name = 'crud_produk'

urlpatterns = [
    path('list-produk', views.listProduk, name='list-produk'),
]
