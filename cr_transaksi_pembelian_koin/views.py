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

def listPaketKoin(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        role = ''
        cursor.execute("SET SEARCH_PATH TO HIDAY")

        try:
            
            if (request.session['role'] == ['admin']):                
                cursor.execute("SELECT * FROM TRANSAKSI_PEMBELIAN_KOIN")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                email = request.session['email'][0]
                cursor.execute("SELECT * FROM transaksi_pembelian_koin WHERE Email ='" + email + "'")
                result = cursor.fetchone()
                
                # cursor.execute("SELECT * FROM transaksi_pembelian_koin WHERE transaksi_pembelian_koin.Email = '"+ email +"'")
                # result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'list_transaksi_paket_koin.html', {"result" : result, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def formPaketKoin(request):
    role = ''
    
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    return render(request, 'form_paket_koin.html', {'form' : FormPaketKoin, "role" : role})

