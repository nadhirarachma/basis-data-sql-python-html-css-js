from multiprocessing import context
from django.shortcuts import render, get_object_or_404
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
            cursor.execute("SELECT PRO.nama AS nama, A.nama AS namaAset, durasi, jumlah_unit_hasil, PRO.id FROM PRODUKSI P JOIN ASET A ON P.Id_alat_produksi = A.id JOIN PRODUK PRO ON P.Id_produk_makanan = PRO.id")
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

def detailProduksi(request, slug):
    cursor = connection.cursor()
    result = []
    result2 = []
    cursor.execute("SET SEARCH_PATH TO HIDAY")
    cursor.execute("SELECT PRO.nama AS nama, A.nama AS namaAset, durasi, jumlah_unit_hasil, PRO.id FROM PRODUKSI P JOIN ASET A ON P.Id_alat_produksi = A.id JOIN PRODUK PRO ON P.Id_produk_makanan = PRO.id WHERE PRO.id = '" + ''.join(slug) + "'")
    result = cursor.fetchone()
    id_produk = result[4]
    print(result[4])

    cursor.execute("SELECT Id_produk_makanan, P.nama as Bahan, Jumlah FROM PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN PD, PRODUK P WHERE PD.id_produk = P.id AND PD.id_produk_makanan = '" + ''.join(id_produk) + "'")
    result2 = tupleFetch(cursor)

    cursor.close()
    temp = {}
    for i in range(len(result2)):
        temp[i+1] = result2[i]
    resultNum = list(temp.items())

    context = {
        'nama' : result[0],
        'namaaset' : result[1],
        'durasi' : result[2],
        'jumlah_unit_hasil' : result[3]
    }

    return render(request, "detail_produksi.html", {"result2": resultNum, "res": context})

def ubahProduksi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_produksi.html', {"form" : UbahProduksi, "role" : role})