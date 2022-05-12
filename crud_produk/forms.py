from django import forms

class BuatProduk(forms.Form):
    JenisProduk = forms.CharField(label='Jenis', max_length=50)
    Nama = forms.CharField(label='Nama', max_length=50)
    HargaJual = forms.CharField(label='Harga', max_length=50)
    SifatProduk = forms.CharField(label='Sifat', max_length=50)