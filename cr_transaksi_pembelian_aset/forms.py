from django import forms

class BuatTransaksiPembelianAset(forms.Form):
    Jumlah = forms.CharField(label='Jumlah', max_length=50)
   