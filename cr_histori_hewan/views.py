from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from datetime import datetime

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
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
            else:
                role = "pengguna"
            cursor.execute("select a.nama, kama.id_aset, kama.jumlah from hiday.koleksi_aset_memiliki_aset kama join hiday.aset a on kama.id_aset = a.id where id_koleksi_aset = '"+ request.session['email'][0] +"' and id in (select id_aset from hiday.hewan);")
            result = tuple_fetch(cursor)

            if request.method == 'POST':
                nama_hewan = request.POST["nama_hewan"]
                jumlah = int(request.POST["jumlah"])
                xp = jumlah*5
                id_hewan = ""

                jumlah_hewan = 0

                for i in result:
                    if i[0] == nama_hewan:
                        jumlah_hewan = i[2]
                        id_hewan = i[1]

                if jumlah <= 0 or jumlah_hewan < jumlah:
                    return render(request, 'create_hewan_error.html')
                else:
                    time_str = str(datetime.now())
                    cursor.execute("insert into hiday.histori_produksi values('" + request.session['email'][0] + "', '" + time_str + "'::timestamp, '" + time_str + "'::timestamp, " + str(jumlah) + ", " + str(xp) + ")")
                    cursor.execute("insert into hiday.histori_hewan values('" + request.session['email'][0] + "', '" + time_str + "'::timestamp, '" + id_hewan + "')")
                    return HttpResponseRedirect('/cr-histori-hewan/list-histori-hewan')

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'produksi_hewan.html', {"result" : result, "role" : role})

    else:
        return HttpResponseRedirect('/login')
