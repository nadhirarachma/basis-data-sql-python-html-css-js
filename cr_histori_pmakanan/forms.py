from django import forms

class BuatProduk(forms.Form):
    IdProduk = forms.CharField(label='IdProduk', max_length=5)
    Jumlah = forms.IntegerField(label='Jumlah')