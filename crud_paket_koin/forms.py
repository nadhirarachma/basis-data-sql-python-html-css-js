from django import forms

class BuatPaketKoin(forms.Form):
    JumlahKoin = forms.IntegerField(label='Jumlah')
    Harga = forms.IntegerField(label='Harga')

class UpdatePaketKoin(forms.Form):
    # JumlahKoin = forms.IntegerField(label='Jumlah')
    Harga = forms.IntegerField(label='Harga')

class DeletePaketKoin(forms.Form):
    JumlahKoin = forms.IntegerField(label='Jumlah')