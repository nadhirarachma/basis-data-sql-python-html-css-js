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
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                # cursor.execute("SELECT * FROM ADMIN WHERE EMAIL = '"+ request.session['email'][0] +"'")
                cursor.execute("SELECT * FROM PAKET_KOIN")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM PAKET_KOIN")
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

        return render(request, 'list_paket_koin.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatPaketKoin(request):
    role = ''
    
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    return render(request, 'create_paket_koin.html', {'form' : BuatPaketKoin, "role" : role})

def updatePaketKoin(request):
    role = ''
    
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    return render(request, 'update_paket_koin.html', {'form' : UpdatePaketKoin, "role" : role})
