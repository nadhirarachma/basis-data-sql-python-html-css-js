from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('viewMessage', views.loggedInView, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.login, name='home'),
]
