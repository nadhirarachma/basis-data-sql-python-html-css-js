from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listProduksi(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        role =''
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            cursor.execute("SELECT PRO.nama AS nama, A.nama AS namaAset, durasi, jumlah_unit_hasil FROM PRODUKSI P JOIN ASET A ON P.Id_alat_produksi = A.id JOIN PRODUK PRO ON P.Id_produk_makanan = PRO.id")
            result = tupleFetch(cursor)
            if (request.session['role'] == ['admin']):        
                role = "admin"

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_produksi.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatProduksi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_produksi.html', {"form" : BuatProduksi, "role" : role})

def detailProduksi(request, pk):
    cursor = connection.cursor()
    result = []
    cursor.execute("SET SEARCH_PATH TO HIDAY")
    cursor.execute("SELECT * FROM PRODUKSI")
    result = tupleFetch(cursor)
    resultt = result[pk+1]

    cursor.close()

    temp = {}
    for i in range(len(result)-1):
        temp[i+1] = result[i]
    resultNum = list(temp.items())
    
    return render(request, 'detail_produksi.html', {"res" : resultNum[pk]})

def ubahProduksi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_produksi.html', {"form" : UbahProduksi, "role" : role})