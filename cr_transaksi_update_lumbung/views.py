from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *
from main.forms import LoginForm

# Create your views here.

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listTransaksiLumbung(request):
    # result = []
    # FormLogin = LoginForm(request.POST)

    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        # role = ''
        
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):                
                cursor.execute("SELECT * FROM hiday.TRANSAKSI_UPGRADE_LUMBUNG")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                email = request.session['email'][0]
                cursor.execute("SELECT * FROM hiday.TRANSAKSI_UPGRADE_LUMBUNG WHERE email='" + email + "'")
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

        return render(request, 'list_transaksi_lumbung.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def formUpgradeLumbung(request):
    role = ''
    
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    return render(request, 'form_upgrade_lumbung.html', {'form' : FormUpgradeLumbung, "role" : role})

