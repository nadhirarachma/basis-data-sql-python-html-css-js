from django import forms

class BuatProduksi(forms.Form):
    IdProduk = forms.CharField(label='IdProduk', max_length=5)
    Jumlah = forms.IntegerField(label='Jumlah')
    XP = forms.IntegerField(label='XP')