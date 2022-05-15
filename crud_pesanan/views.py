from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

# Create your views here.

def tuple_fetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def list_histori_pesanan(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM PESANAN;")
                result = tuple_fetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM PESANAN;")
                result = tuple_fetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'list_histori_pesanan.html', {"result" : result, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def view_detail_pesanan(request, id):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result1 = []
        result2 = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            cursor.execute("SELECT id, nama, jenis, total, status FROM pesanan WHERE id = '" + id +"';")
            result1 = tuple_fetch(cursor)

            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT p.nama, dp.jumlah, dp.subtotal FROM detail_pesanan dp JOIN produk p on dp.id_produk = p.id WHERE dp.id_pesanan = '" + id +"';")
                result2 = tuple_fetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT p.nama, dp.jumlah, dp.subtotal FROM detail_pesanan dp JOIN produk p on dp.id_produk = p.id WHERE dp.id_pesanan = '" + id +"';")
                result2 = tuple_fetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'detaiL_pesanan.html', {"result1" : result1, "result2" : result2, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def buat_pesanan(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_pesanan.html', {"form" : buat_pesanan_form, "role" : role})

def ubah_pesanan(request, id):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result1 = []
        result2 = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            cursor.execute("SELECT id, nama, jenis, total, status FROM pesanan WHERE id = '" + id +"';")
            result1 = tuple_fetch(cursor)

            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT p.nama, dp.jumlah, dp.subtotal FROM detail_pesanan dp JOIN produk p on dp.id_produk = p.id WHERE dp.id_pesanan = '" + id +"';")
                result2 = tuple_fetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT p.nama, dp.jumlah, dp.subtotal FROM detail_pesanan dp JOIN produk p on dp.id_produk = p.id WHERE dp.id_pesanan = '" + id +"';")
                result2 = tuple_fetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_pesanan.html', {"form": ubah_pesanan_form, "result1" : result1, "result2" : result2, "role" : role})

    else:
        return HttpResponseRedirect('/login')

