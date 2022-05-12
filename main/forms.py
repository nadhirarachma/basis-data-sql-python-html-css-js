from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='E-mail', max_length=50)
    password = forms.CharField(label='Password', max_length=50)