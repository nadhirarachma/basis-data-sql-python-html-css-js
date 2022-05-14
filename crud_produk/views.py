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
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                # cursor.execute("SELECT * FROM ADMIN WHERE EMAIL = '"+ request.session['email'][0] +"'")
                cursor.execute("SELECT * FROM PRODUK")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM PRODUK")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)-1):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_produk.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listProduksi(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                # cursor.execute("SELECT * FROM ADMIN WHERE EMAIL = '"+ request.session['email'][0] +"'")
                cursor.execute("SELECT * FROM PRODUKSI")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM PRODUKSI")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)-1):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

        return render(request, 'list_produksi.html', {"result" : resultNum, "role" : role})

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

def buatProduksi(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_produksi.html', {"form" : BuatProduksi, "role" : role})