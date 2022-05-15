from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def listAset(request):
    if request.session.has_key('email'):
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"

            else:
                role = "pengguna"
        
        except Exception as e:
            print(e)
            
        return render(request, 'list_aset.html', {"role" : role})

    else:
        return HttpResponseRedirect('/login')

def listDekorasi(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM ASET JOIN DEKORASI ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM ASET JOIN DEKORASI ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_dekorasi.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listBibitTanaman(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM ASET JOIN BIBIT_TANAMAN ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM ASET JOIN BIBIT_TANAMAN ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_bibit_tanaman.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listKandang(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM ASET JOIN KANDANG ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM ASET JOIN KANDANG ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_kandang.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listHewan(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT HEWAN.ID_Aset, nama, minimum_level, harga_beli, durasi_produksi, id_kandang FROM ASET JOIN HEWAN ON HEWAN.ID_Aset=ASET.ID JOIN KANDANG ON HEWAN.ID_Kandang=KANDANG.ID_Aset")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT HEWAN.ID_Aset, nama, minimum_level, harga_beli, durasi_produksi, id_kandang FROM ASET JOIN HEWAN ON HEWAN.ID_Aset=ASET.ID JOIN KANDANG ON HEWAN.ID_Kandang=KANDANG.ID_Aset")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_hewan.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listAlatProduksi(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM ASET JOIN ALAT_PRODUKSI ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM ASET JOIN ALAT_PRODUKSI ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_alat_produksi.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listPetakSawah(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM ASET JOIN PETAK_SAWAH ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM ASET JOIN PETAK_SAWAH ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_petak_sawah.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatAset(request):
    if request.session.has_key('email'):
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"

            else:
                role = "pengguna"
        
        except Exception as e:
            print(e)
            
        return render(request, 'buat_aset.html', {"role" : role})

    else:
        return HttpResponseRedirect('/login')

def buatDekorasi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_dekorasi.html', {"form" : BuatDekorasi, "role" : role})

def buatBibitTanaman(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_bibit_tanaman.html', {"form" : BuatBibitTanaman, "role" : role})

def buatKandang(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_kandang.html', {"form" : BuatKandang, "role" : role})

def buatHewan(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_hewan.html', {"form" : BuatHewan, "role" : role})

def buatAlatProduksi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_alat_produksi.html', {"form" : BuatAlatProduksi, "role" : role})

def buatPetakSawah(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_petak_sawah.html', {"form" : BuatPetakSawah, "role" : role})

def ubahDekorasi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_dekorasi.html', {"form" : UbahDekorasi, "role" : role})

def ubahBibitTanaman(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_bibit_tanaman.html', {"form" : UbahBibitTanaman, "role" : role})

def ubahKandang(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_kandang.html', {"form" : UbahKandang, "role" : role})

def ubahHewan(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_hewan.html', {"form" : UbahHewan, "role" : role})

def ubahAlatProduksi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_alat_produksi.html', {"form" : UbahAlatProduksi, "role" : role})

def ubahPetakSawah(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_petak_sawah.html', {"form" : UbahPetakSawah, "role" : role})
