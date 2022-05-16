from email.policy import default
from django import forms

class FormProduksiTanaman(forms.Form):
    BibitTanaman = forms.CharField(label='Bibit Tanaman')
    Jumlah = forms.IntegerField(label='Jumlah')    
    XP = forms.IntegerField(label='XP')
    # CaraPembayaran = forms.CharField(label='Cara Pembayaran', max_length=50)

# class UpdatePaketKoin(forms.Form):
#     JumlahKoin = forms.IntegerField(label='Jumlah')
#     Harga = forms.IntegerField(label='Harga')