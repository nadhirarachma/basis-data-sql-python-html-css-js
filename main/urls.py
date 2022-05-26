from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='landing'),
    path('registrasi', views.registrasi, name='registrasi'),
    path('registrasi-pengguna', views.registrasiPengguna, name='registrasi-pengguna'),
    path('registrasi-admin', views.registrasiAdmin, name='registrasi-admin'),
    path('login', views.login, name='login'),
    path('profile', views.loggedInView, name='view'),
    path('logout', views.logout, name='logout'),
    path('index', views.login, name='home'),
    path('isi-lumbung', views.isiLumbung, name='isi-lumbung'),
]
