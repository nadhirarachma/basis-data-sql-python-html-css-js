from time import time
from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listHistori(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        role =''
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            
            if (request.session['role'] == ['admin']):    
                cursor.execute("SELECT HP.email, HP.waktu_awal, HP.waktu_selesai, HP.jumlah, HP.xp, P.nama as namaproduk, A.nama as asetalat from hiday.HISTORI_PRODUKSI HP JOIN hiday.HISTORI_PRODUKSI_MAKANAN HPM ON HP.email = HPM.email AND HP.waktu_awal = HPM.waktu_awal JOIN hiday.PRODUK P ON HPM.id_produk_makanan = P.id JOIN hiday.ASET A ON HPM.id_alat_produksi = A.id")
                result = tupleFetch(cursor)    
                role = "admin"

            else:
                email = str(request.session['email'][0])
                cursor.execute("SELECT HP.waktu_awal, HP.waktu_selesai, HP.jumlah, HP.xp, P.nama as namaproduk, A.nama as asetalat from hiday.HISTORI_PRODUKSI HP JOIN hiday.HISTORI_PRODUKSI_MAKANAN HPM ON HP.email = HPM.email AND HP.waktu_awal = HPM.waktu_awal JOIN hiday.PRODUK P ON HPM.id_produk_makanan = P.id JOIN hiday.ASET A ON HPM.id_alat_produksi = A.id AND HPM.email  = '" + ''.join(email) + "'")
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

        return render(request, 'list_histori_pmakanan.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatProduksi(request):
    # if (request.session['role'] == ['admin']):
    #     role = "admin"

    # else:
    #     role = "pengguna"
    
    # return render(request, 'buat_histori_pmakanan.html', {"form" : BuatProduk, "role" : role})

    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                return render(request, 'buat_histori_pmakanan.html', {"form" : BuatProduksi, "role" : role})

            else:
                role = "pengguna"
                form = BuatProduksi(request.POST, request.FILES)
                cursor = connection.cursor()
                result = []

                cursor.execute("SET SEARCH_PATH TO HIDAY")
                cursor.execute("SELECT id, nama FROM PRODUK")
                result = tupleFetch(cursor)
                cursor.execute("SET SEARCH_PATH TO public")

                print(result)

                # context = {
                #     'id' : result[0],
                #     'nama' : result[1],
                #     'hargajual' : result[2],
                #     'sifat' : result[3],
                #     'jenisproduk' : result[4]
                # }

                if (form.is_valid and request.method == 'POST'):
                    idproduk = form.data.get("IdProduk")
                    jumlah = form.data.get("Jumlah")
                    xp = form.data.get("XP")

                    print(idproduk)
                    print(jumlah)
                    print(xp)

                    email = request.session['email'][0]

                    cursor.execute("SET SEARCH_PATH TO HIDAY")

                    cursor.execute("SELECT jumlah, id_produk FROM PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN WHERE id_produk_makanan = '" + idproduk + "'")
                    result = cursor.fetchone()

                    jumlahdibutuhkan = result[0]
                    produkdibutuhkan = result[1]
                    print(jumlahdibutuhkan)
                    print(produkdibutuhkan)

                    cursor.execute("SELECT jumlah FROM LUMBUNG_MEMILIKI_PRODUK WHERE id_lumbung = '" + email + "' AND id_produk = '" + produkdibutuhkan + "'")
                    result = cursor.fetchone()

                    jumlahdipengguna = result[0]
                    print(jumlahdipengguna)

                    cursor.execute("SELECT id_alat_produksi FROM PRODUKSI WHERE id_produk_makanan = '" + idproduk + "'")
                    result = cursor.fetchone()

                    alatproduksi = result[0]
                    print(alatproduksi)

                    

                    # if ((jumlahdipengguna > jumlahdibutuhkan * jumlah)):
                        

                    cursor.execute("INSERT INTO ")
                    cursor.execute("SET SEARCH_PATH TO public")
                    cursor.close()

                    return HttpResponseRedirect('/crud-produk/list-produk')

                return render(request, 'buat_histori_pmakanan.html', {"form" : BuatProduksi, "role" : role, "result" : result})
            
        except Exception as e:
            print(e)            
        
    else:
        return HttpResponseRedirect('/login')