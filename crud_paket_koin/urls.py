from django.urls import path

from . import views

app_name = 'crud_paket_koin'

urlpatterns = [
    path('list-paket-koin', views.listPaketKoin, name='list-paket-koin'),
    path('create-paket-koin', views.buatPaketKoin, name='create-paket-koin'),
    path('update-paket-koin/<slug:slug>', views.updatePaketKoin, name='update-paket-koin'),
    path('delete-paket-koin/<slug:slug>', views.deletePaketKoin, name='delete-paket-koin'),
]
