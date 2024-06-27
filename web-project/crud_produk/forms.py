from django import forms

class BuatProduk(forms.Form):
    IdProduk = forms.CharField(label='ID', max_length=5)
    Nama = forms.CharField(label='Nama', max_length=50)
    HargaJual = forms.IntegerField(label='Harga')
    SifatProduk = forms.CharField(label='Sifat', max_length=20)

class UbahProduk(forms.Form):
    HargaJual = forms.IntegerField(label='Harga')
    SifatProduk = forms.CharField(label='Sifat', max_length=20)