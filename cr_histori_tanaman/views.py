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

def listHistoriProduksiTanaman(request):
    # result = []
    # FormLogin = LoginForm(request.POST)

    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        role = ''
        
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):                
                cursor.execute("SELECT * FROM TRANSAKSI_UPGRADE_LUMBUNG")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                email = request.session['email'][0]
                cursor.execute("SELECT HT.email, HT.waktu_awal :: time as Waktu_awal, Hp.waktu_selesai :: time as Waktu_selesai, HP.jumlah, HP.xp, A.nama FROM HISTORI_TANAMAN AS HT, HISTORI_PRODUKSI AS HP, BIBIT_TANAMAN AS BT, ASET AS A WHERE HT.email = HP.email AND HT.waktu_awal=HP.waktu_awal AND HT.id_bibit_tanaman =BT.id_aset AND BT.id_aset=A.id AND HT.email='" + email + "'")
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

        return render(request, 'list_histori_produksi_tanaman.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def formProduksiTanaman(request):
    role = ''
    
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    return render(request, 'form_produksi_tanaman.html', {'form' : FormProduksiTanaman, "role" : role})

