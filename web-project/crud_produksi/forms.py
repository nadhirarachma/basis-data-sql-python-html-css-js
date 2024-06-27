from django import forms

class BuatProduksi(forms.Form):
    IdAlat = forms.CharField(label='IdAlat', max_length=5)
    IdProduk = forms.CharField(label='IdProduk', max_length=5)
    Durasi = forms.TimeField(label='Durasi')
    Jumlah = forms.IntegerField(label='Jumlah')

class BahanProduksi(forms.Form):
    IdProduk = forms.CharField(label='IdProduk', max_length=5)
    Jumlah = forms.IntegerField(label='Jumlah')

class UbahProduksi(forms.Form):
    IdAlat = forms.CharField(label='IdAlat', max_length=5)
    IdProduk = forms.CharField(label='IdProduk', max_length=5)
    Durasi = forms.TimeField(label='Durasi')
    Jumlah = forms.IntegerField(label='Jumlah')