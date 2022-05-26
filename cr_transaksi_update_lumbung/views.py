from pickle import NONE
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
    if (request.session['role'] == ['pengguna']):
        role = "pengguna"
        # print('uuu')
        # form = FormPaketKoin(request.POST, request.FILES)
        cursor = connection.cursor()
        result = []
        email = request.session['email'][0]

        cursor.execute("SELECT *  FROM hiday.LUMBUNG WHERE email = '" + ''.join(email) + "'")
        result = cursor.fetchone()

        # print('aaa')
        if (result == None):
            level_lumbung = 1
            kapasitas_lumbung = 50
        
        else:
            context = {
                'level' : result[1],
                'kapasitas_maksimal' : result[2],
            }

            level_lumbung = int(context['level']) + 1
            kapasitas_lumbung = int(context['kapasitas_maksimal']) + 50

        context = {
            'level' : level_lumbung,
            'kapasitas_maksimal' : kapasitas_lumbung
        }

        if (request.method == 'POST'):

            email = request.session['email'][0]
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            

            try:
                
                cursor.execute("SELECT * FROM hiday.PENGGUNA WHERE email = '" + ''.join(email) + "'")
                resultt = cursor.fetchone()
                contextt = {
                    'koin' : resultt[4]
                }

                koinPengguna = int(contextt['koin'])

                if(koinPengguna >= 200) :
                    print('bisa')
                    cursor.execute("UPDATE hiday.LUMBUNG SET level="+ str(level_lumbung) +", kapasitas_maksimal ="+ str(kapasitas_lumbung)+" WHERE email = '" + ''.join(email) + "';")
                    cursor.execute("INSERT INTO hiday.TRANSAKSI_UPGRADE_LUMBUNG VALUES('"+str(email)+"', '"+dt+"');")
                
                elif (koinPengguna < 200):
                    print("gk cukup")
                    return HttpResponseNotFound("Koin anda tidak cukup, silahkan cari Koin terlebih dahulu")

            
            except Exception as e:
                print('gak bisa')
                print(e)
                cursor.close()

            finally:
                cursor.close()
            return HttpResponseRedirect('/cr-transaksi-upgrade-lumbung/list-transaksi-lumbung')

        
        return render(request, 'form_upgrade_lumbung.html', {"role" : role, "result" : context})
    
    else:
        role = "admin"

    return render(request, 'form_upgrade_lumbung.html', { "role" : role, "result" : context})

