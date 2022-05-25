from turtle import st
from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *
from main.forms import LoginForm
import datetime

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
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):                
                cursor.execute("SELECT HT.email, HT.waktu_awal :: time as Waktu_awal, Hp.waktu_selesai :: time as Waktu_selesai, HP.jumlah, HP.xp, A.nama FROM hiday.HISTORI_TANAMAN AS HT, hiday.HISTORI_PRODUKSI AS HP, hiday.BIBIT_TANAMAN AS BT, hiday.ASET AS A WHERE HT.email = HP.email AND HT.waktu_awal=HP.waktu_awal AND HT.id_bibit_tanaman =BT.id_aset AND BT.id_aset=A.id")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                email = request.session['email'][0]
                cursor.execute("SELECT HT.email, HT.waktu_awal :: time as Waktu_awal, Hp.waktu_selesai :: time as Waktu_selesai, HP.jumlah, HP.xp, A.nama FROM hiday.HISTORI_TANAMAN AS HT, hiday.HISTORI_PRODUKSI AS HP, hiday.BIBIT_TANAMAN AS BT, hiday.ASET AS A WHERE HT.email = HP.email AND HT.waktu_awal=HP.waktu_awal AND HT.id_bibit_tanaman =BT.id_aset AND BT.id_aset=A.id AND HT.email='" + email + "'")
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

    if (request.session['role'] == ['pengguna']):
        form = FormProduksiTanaman(request.POST, request.FILES)
        role = "pengguna"
        cursor = connection.cursor()
        result = []
        email = request.session['email'][0]

        cursor.execute("SELECT id, nama FROM hiday.ASET WHERE id IN (SELECT id_aset FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET WHERE id_koleksi_aset = '" + ''.join(email) + "' AND id_aset LIKE '%BT%');")
        result = tupleFetch(cursor)


        if (form.is_valid and request.method == 'POST'):
            jumlah_produksi = form.data.get('Jumlah')
            jumlah_produksi_int = int(jumlah_produksi)
            email = request.session['email'][0]
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            id_bibit = form.data.get('IdProduk')

            jumlah_bibit = ''
            cursor.execute("SELECT jumlah FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET WHERE id_aset='" + str(id_bibit)+"' AND id_koleksi_aset = '" + ''.join(email)+"';")
            jumlah_bibit = cursor.fetchone()
            print(jumlah_bibit)
            jumlah_bibit_int = int(jumlah_bibit[0])
            print(jumlah_bibit_int)

            xp = 5*jumlah_bibit_int
            
            if (jumlah_produksi_int <= jumlah_bibit_int):
                try:
                    print('bisa')
                    cursor.execute("INSERT INTO hiday.HISTORI_PRODUKSI VALUES('"+str(email)+"', '"+str(dt)+"' , '"+ str(dt) +"' , "+str(jumlah_bibit_int)+" , "+ str(xp)+");")
                    cursor.execute("INSERT INTO hiday.HISTORI_TANAMAN VALUES('"+str(email)+"', '"+str(dt)+"' , '"+ str(id_bibit)+"' );")
            
                except Exception as e:
                    print('gak bisa')
                    print(e)
                    cursor.close()

                finally:
                    cursor.close()
                return HttpResponseRedirect('/cr-histori-tanaman/list-histori-tanaman')
                
                
            else:
                return HttpResponseNotFound("Anda tidak memiliki bibit yang cukup, silahkan membeli bibit terlebih dahulu")
            
                    
        return render(request, 'form_produksi_tanaman.html', {"role" : role, "result" : result})
    
    else:
        role = "admin"

    return render(request, 'form_produksi_tanaman.html', { "role" : role, "result" : result})

