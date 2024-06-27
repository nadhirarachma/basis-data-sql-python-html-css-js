from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='E-mail', max_length=50)
    password = forms.CharField(label='Password', max_length=25)

class PenggunaForm(forms.Form):
    email = forms.CharField(label='E-mail', max_length=50)
    password = forms.CharField(label='Password', max_length=25)
    namaAreaPertanian = forms.CharField(label='Nama Area Pertanian', max_length=25)

class AdminForm(forms.Form):
    email = forms.CharField(label='E-mail', max_length=50)
    password = forms.CharField(label='Password', max_length=25)