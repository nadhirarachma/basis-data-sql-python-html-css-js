from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listHistori(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        role =''
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            
            if (request.session['role'] == ['admin']):    
                cursor.execute("SELECT HP.email, HP.waktu_awal, HP.waktu_selesai, HP.jumlah, HP.xp, P.nama as namaproduk, A.nama as asetalat from HISTORI_PRODUKSI HP JOIN HISTORI_PRODUKSI_MAKANAN HPM ON HP.email = HPM.email AND HP.waktu_awal = HPM.waktu_awal JOIN PRODUK P ON HPM.id_produk_makanan = P.id JOIN ASET A ON HPM.id_alat_produksi = A.id")
                result = tupleFetch(cursor)    
                role = "admin"

            else:
                email = str(request.session['email'][0])
                cursor.execute("SELECT HP.waktu_awal, HP.waktu_selesai, HP.jumlah, HP.xp, P.nama as namaproduk, A.nama as asetalat from HISTORI_PRODUKSI HP JOIN HISTORI_PRODUKSI_MAKANAN HPM ON HP.email = HPM.email AND HP.waktu_awal = HPM.waktu_awal JOIN PRODUK P ON HPM.id_produk_makanan = P.id JOIN ASET A ON HPM.id_alat_produksi = A.id AND HPM.email  = '" + ''.join(email) + "'")
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

        return render(request, 'list_histori_pmakanan.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatProduk(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_histori_pmakanan.html', {"form" : BuatProduk, "role" : role})