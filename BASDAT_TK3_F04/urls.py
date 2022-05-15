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
    path('crud-pesanan/', include('crud_pesanan.urls')),
    path('cr-histori-hewan/', include('cr_histori_hewan.urls')),
    path('cr-histori-penjualan/', include('cr_histori_penjualan.urls')),
    path('crud-produksi/', include('crud_produksi.urls')),
    path('cr-histori-pmakanan/', include('cr_histori_pmakanan.urls'))
]
