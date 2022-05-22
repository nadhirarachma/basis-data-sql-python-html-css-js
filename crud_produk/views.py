from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listProduk(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            cursor.execute("SELECT id, nama, harga_jual, sifat_produk, CASE WHEN id LIKE '%HP%' THEN 'Hasil Panen' WHEN id LIKE '%PH%' THEN 'Produk Hewan' WHEN id LIKE '%PM%' THEN 'Produk Makanan' END AS jenisproduk FROM hiday.PRODUK")
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

        return render(request, 'list_produk.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatProduk(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_produk.html', {"form" : BuatProduk, "role" : role})

def ubahProduk(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'ubah_produk.html', {"form" : UbahProduk, "role" : role})