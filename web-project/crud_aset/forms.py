from django import forms

class BuatDekorasi(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    HargaJual = forms.IntegerField(label='HargaJual')

class BuatBibitTanaman(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    DurasiPanen = forms.TimeField(label='DurasiPanen')

class BuatKandang(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    KapasitasMaks = forms.IntegerField(label='KapasitasMaks')
    JenisHewan = forms.CharField(label='JenisHewan', max_length=50)

class BuatHewan(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    DurasiProduksi = forms.TimeField(label='DurasiProduksi')

class BuatAlatProduksi(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    KapasitasMaks = forms.IntegerField(label='KapasitasMaks')

class BuatPetakSawah(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')

class UbahDekorasi(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50, disabled=True, required=False)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    HargaJual = forms.IntegerField(label='HargaJual')

class UbahBibitTanaman(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50, disabled=True, required=False)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    DurasiPanen = forms.TimeField(label='DurasiPanen')

class UbahKandang(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50, disabled=True, required=False)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    KapasitasMaks = forms.IntegerField(label='KapasitasMaks')
    JenisHewan = forms.CharField(label='JenisHewan', max_length=50, disabled=True, required=False)

class UbahHewan(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50, disabled=True, required=False)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    DurasiProduksi = forms.TimeField(label='DurasiProduksi')
    IDKandang = forms.CharField(label='IDKandang', max_length=5, disabled=True, required=False)

class UbahAlatProduksi(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50, disabled=True, required=False)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
    KapasitasMaks = forms.IntegerField(label='KapasitasMaks')

class UbahPetakSawah(forms.Form):
    ID = forms.CharField(label='ID', max_length=5, disabled=True, required=False)
    Nama = forms.CharField(label='Nama', max_length=50, disabled=True, required=False)
    MinimumLevel = forms.IntegerField(label='MinimumLevel')
    HargaBeli = forms.IntegerField(label='HargaBeli')
