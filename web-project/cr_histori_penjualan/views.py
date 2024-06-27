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

def list_histori_penjualan(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.HISTORI_PENJUALAN;")
                result = tuple_fetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM hiday.HISTORI_PENJUALAN WHERE email = '"+ request.session['email'][0] +"'")
                result = tuple_fetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'list_histori_penjualan.html', {"result" : result, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def view_detail_penjualan(request, id):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result1 = []
        result2 = []
        result3 = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
            else:
                role = "pengguna"
            cursor.execute("SELECT email, waktu_penjualan FROM hiday.histori_penjualan WHERE id_pesanan = '" + id +"';")
            result1 = tuple_fetch(cursor)

            cursor.execute("SELECT id, nama, jenis, total, status FROM hiday.pesanan WHERE id = '" + id +"';")
            result2 = tuple_fetch(cursor)

            cursor.execute("SELECT p.nama, dp.jumlah, dp.subtotal FROM hiday.detail_pesanan dp JOIN hiday.produk p on dp.id_produk = p.id WHERE dp.id_pesanan = '" + id +"';")
            result3 = tuple_fetch(cursor)

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'detaiL_penjualan.html', {"result1" : result1, "result2" : result2, "result3" : result3, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def ambil_pesanan(request, id):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        selected_pesanan = []
        try:
            if (request.session['role'] == ['pengguna']):
                cursor.execute("select id, total from hiday.pesanan where id = '" + id + "'")
                selected_pesanan = tuple_fetch(cursor)
                time_str = str(datetime.now())
                cursor.execute("insert into hiday.histori_penjualan values('" + request.session['email'][0] + "', '" + time_str + "'::timestamp, '" + str(selected_pesanan[0][1]) + "', 10, '" + selected_pesanan[0][0] + "')")    

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return HttpResponseRedirect('/cr-histori-penjualan/list-histori-penjualan')

    else:
        return HttpResponseRedirect('/login')
