from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login, name='loginn'),
    path('login', views.login, name='login'),
    path('profile', views.loggedInView, name='view'),
    path('logout', views.logout, name='logout'),
    path('index', views.login, name='home'),
    path('isi-lumbung', views.isiLumbung, name='isi-lumbung'),
]
