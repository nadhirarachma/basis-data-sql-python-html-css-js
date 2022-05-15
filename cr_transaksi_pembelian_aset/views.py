from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def listTransaksiPembelianAset(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT ID_Aset, email, waktu, jumlah, nama, harga_beli * jumlah as total_harga, CASE WHEN ID_Aset LIKE 'DK%' THEN 'Dekorasi' WHEN ID_Aset LIKE 'BT%' THEN 'Bibit Tanaman' WHEN ID_Aset LIKE 'KD%' THEN 'Kandang' WHEN ID_Aset LIKE 'HW%' THEN 'Hewan' WHEN ID_Aset LIKE 'AP%' THEN 'Alat Produksi' WHEN ID_Aset LIKE 'PS%' THEN 'Petak Sawah' END AS jenis_aset FROM TRANSAKSI_PEMBELIAN JOIN ASET ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT ID_Aset, waktu, jumlah, nama, harga_beli * jumlah as total_harga, CASE WHEN ID_Aset LIKE 'DK%' THEN 'Dekorasi' WHEN ID_Aset LIKE 'BT%' THEN 'Bibit Tanaman' WHEN ID_Aset LIKE 'KD%' THEN 'Kandang' WHEN ID_Aset LIKE 'HW%' THEN 'Hewan' WHEN ID_Aset LIKE 'AP%' THEN 'Alat Produksi' WHEN ID_Aset LIKE 'PS%' THEN 'Petak Sawah' END AS jenis_aset FROM TRANSAKSI_PEMBELIAN JOIN ASET ON ID_Aset=ID WHERE email= '" + request.session['email'][0] +"'")
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

        return render(request, 'list_transaksi_pembelian_aset.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatTransaksiPembelianAset(request):
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"
    
    return render(request, 'buat_transaksi_pembelian_aset.html', {"form" : BuatTransaksiPembelianAset, "role" : role})
