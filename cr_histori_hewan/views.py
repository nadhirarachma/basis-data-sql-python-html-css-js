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

def list_histori_hewan(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                # cursor.execute("SELECT * FROM ADMIN WHERE EMAIL = '"+ request.session['email'][0] +"'")
                cursor.execute("select hp.email, hp.waktu_awal, hp.waktu_selesai, hp.jumlah, hp.xp, a.nama from hiday.histori_produksi hp JOIN hiday.histori_hewan hh on hp.email = hh.email and hp.waktu_awal = hh.waktu_awal JOIN hiday.hewan h on hh.id_hewan = h.id_aset JOIN hiday.aset a on h.id_aset = a.id;")
                result = tuple_fetch(cursor)
                role = "admin"

            else:
                cursor.execute("select hp.waktu_awal, hp.waktu_selesai, hp.jumlah, hp.xp, a.nama from hiday.histori_produksi hp JOIN hiday.histori_hewan hh on hp.email = hh.email and hp.waktu_awal = hh.waktu_awal JOIN hiday.hewan h on hh.id_hewan = h.id_aset JOIN hiday.aset a on h.id_aset = a.id WHERE hh.email = '"+ request.session['email'][0] +"'")
                result = tuple_fetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'list_histori_hewan.html', {"result" : result, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def produksi_hewan(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'produksi_hewan.html', {"form" : produksi_hewan_form, "role" : role})

