from django import forms

class BuatDekorasi(forms.Form):
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    HargaJual = forms.CharField(label='HargaJual', max_length=50)

class BuatBibitTanaman(forms.Form):
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    DurasiPanen = forms.CharField(label='DurasiPanen', max_length=50)

class BuatKandang(forms.Form):
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    KapasitasMaks = forms.CharField(label='KapasitasMaks', max_length=50)

class BuatHewan(forms.Form):
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    DurasiProduksi = forms.CharField(label='DurasiProduksi', max_length=50)

class BuatAlatProduksi(forms.Form):
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    KapasitasMaks = forms.CharField(label='KapasitasMaks', max_length=50)

class BuatPetakSawah(forms.Form):
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)

class UbahDekorasi(forms.Form):
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    HargaJual = forms.CharField(label='HargaJual', max_length=50)

class UbahBibitTanaman(forms.Form):
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    DurasiPanen = forms.CharField(label='DurasiPanen', max_length=50)

class UbahKandang(forms.Form):
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    KapasitasMaks = forms.CharField(label='KapasitasMaks', max_length=50)

class UbahHewan(forms.Form):
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    DurasiProduksi = forms.CharField(label='DurasiProduksi', max_length=50)

class UbahAlatProduksi(forms.Form):
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
    KapasitasMaks = forms.CharField(label='KapasitasMaks', max_length=50)

class UbahPetakSawah(forms.Form):
    MinimumLevel = forms.CharField(label='MinimumLevel', max_length=50)
    HargaBeli = forms.CharField(label='HargaBeli', max_length=50)
