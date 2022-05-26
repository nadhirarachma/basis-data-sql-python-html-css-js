from django import forms

class BuatTransaksiPembelianAset(forms.Form):
    Jumlah = forms.IntegerField(label='Jumlah')
   