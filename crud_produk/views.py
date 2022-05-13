from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *
# Create your views here.

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

        return render(request, 'list_produk.html', {"result" : result, "role" : role})

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

        return render(request, 'list_produksi.html', {"result" : result, "role" : role})

   else:
        return HttpResponseRedirect('/login')