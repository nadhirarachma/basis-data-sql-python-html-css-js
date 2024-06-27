from django import forms

class FormPaketKoin(forms.Form):
    # PaketKoin = forms.IntegerField(label='Paket Koin')
    # Harga = forms.IntegerField(label='Harga')    
    Jumlah = forms.IntegerField(label='Jumlah')
    CaraPembayaran = forms.CharField(label='Cara Pembayaran', max_length=50)

# class UpdatePaketKoin(forms.Form):
#     JumlahKoin = forms.IntegerField(label='Jumlah')
#     Harga = forms.IntegerField(label='Harga')