from django import forms

class BuatProduk(forms.Form):
    IdProduk = forms.CharField(label='ID', max_length=5)
    Nama = forms.CharField(label='Nama', max_length=50)
    HargaJual = forms.IntegerField(label='Harga')
    SifatProduk = forms.CharField(label='Sifat', max_length=20)

class UbahProduk(forms.Form):
    IdProduk = forms.CharField(label='ID', max_length=5)
    Nama = forms.CharField(label='Nama', max_length=50)
    HargaJual = forms.IntegerField(label='Harga')
    SifatProduk = forms.CharField(label='Sifat', max_length=20)

class BuatProduksi(forms.Form):
    IdAlat = forms.CharField(label='IdAlat', max_length=5)
    IdProduk = forms.CharField(label='IdProduk', max_length=5)
    Durasi = forms.TimeField(label='Durasi')
    Jumlah = forms.IntegerField(label='Jumlah')