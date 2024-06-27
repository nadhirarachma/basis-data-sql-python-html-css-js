from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *
from datetime import datetime

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def listTransaksiPembelianAset(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT ID_Aset, email, waktu, jumlah, nama, harga_beli * jumlah as total_harga, CASE WHEN ID_Aset LIKE 'DK%' THEN 'Dekorasi' WHEN ID_Aset LIKE 'BT%' THEN 'Bibit Tanaman' WHEN ID_Aset LIKE 'KD%' THEN 'Kandang' WHEN ID_Aset LIKE 'HW%' THEN 'Hewan' WHEN ID_Aset LIKE 'AP%' THEN 'Alat Produksi' WHEN ID_Aset LIKE 'PS%' THEN 'Petak Sawah' END AS jenis_aset FROM hiday.TRANSAKSI_PEMBELIAN JOIN hiday.ASET ON ID_Aset=ID")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT ID_Aset, waktu, jumlah, nama, harga_beli * jumlah as total_harga, CASE WHEN ID_Aset LIKE 'DK%' THEN 'Dekorasi' WHEN ID_Aset LIKE 'BT%' THEN 'Bibit Tanaman' WHEN ID_Aset LIKE 'KD%' THEN 'Kandang' WHEN ID_Aset LIKE 'HW%' THEN 'Hewan' WHEN ID_Aset LIKE 'AP%' THEN 'Alat Produksi' WHEN ID_Aset LIKE 'PS%' THEN 'Petak Sawah' END AS jenis_aset FROM hiday.TRANSAKSI_PEMBELIAN JOIN hiday.ASET ON ID_Aset=ID WHERE email= '" + request.session['email'][0] +"'")
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
    if request.session.has_key('email'):
        cursor = connection.cursor()
        response = {}
        email =  request.session['email'][0]
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            if (request.session['role'] == ['pengguna']):
                role = "pengguna"
                cursor.execute("SELECT ID, nama, harga_beli, minimum_level, CASE WHEN ID LIKE 'DK%' THEN 'Dekorasi' WHEN ID LIKE 'BT%' THEN 'Bibit Tanaman' WHEN ID LIKE 'KD%' THEN 'Kandang' WHEN ID LIKE 'HW%' THEN 'Hewan' WHEN ID LIKE 'AP%' THEN 'Alat Produksi' WHEN ID LIKE 'PS%' THEN 'Petak Sawah' END AS jenis_aset FROM HIDAY.ASET ORDER BY ID")
                response["DetailAset"] = cursor.fetchall()
                response["form"] = BuatTransaksiPembelianAset
                response["role"] = role

                if (request.method == "POST"):
                    form = BuatTransaksiPembelianAset(request.POST or None)
                    if form.is_valid():
                        detail_aset = request.POST['id_detail_aset']
                        jumlah = request.POST['Jumlah']
                        nama = detail_aset.split(" - ")[1]

                        cursor.execute("SELECT ID FROM hiday.ASET WHERE nama= '" + nama +"'")
                        result = tupleFetch(cursor)
                        ID = result[0][0]
                        
                        cursor.execute("INSERT INTO HIDAY.TRANSAKSI_PEMBELIAN VALUES(%s, %s, %s, %s)", [email, waktu, jumlah, ID])

                        return redirect("/cr-transaksi-pembelian-aset/list-transaksi-pembelian-aset")
                    else:
                        return redirect("/cr-transaksi-pembelian-aset/buat-transaksi-pembelian-aset")

            else:
                role = "admin"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_transaksi_pembelian_aset.html', response)


    














