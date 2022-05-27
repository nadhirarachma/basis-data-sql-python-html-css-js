from traceback import print_tb
from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listProduk(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        resultt = []

        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                role = "admin"

                cursor.execute("SELECT id_produk FROM hiday.DETAIL_PESANAN")
                resultt = tupleFetch(cursor)

                cursor.execute("SELECT id_produk FROM hiday.LUMBUNG_MEMILIKI_PRODUK")
                resultt.append(tupleFetch(cursor))

                cursor.execute("SELECT id_produk_hewan FROM hiday.HEWAN_MENGHASILKAN_PRODUK_HEWAN")
                resultt.append(tupleFetch(cursor))

                cursor.execute("SELECT id_hasil_panen FROM hiday.BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN")
                resultt.append(tupleFetch(cursor))

                # print(resultt)
                # dataAdmin = namedtuple('ResultAdmin',result)

                idGabisaDelete = []
                for i in range(len(resultt)):
                    idGabisaDelete.append(resultt[i][0])

                # print(idGabisaDelete)

                cursor.execute("SELECT id, nama, harga_jual, sifat_produk, CASE WHEN id LIKE '%HP%' THEN 'Hasil Panen' WHEN id LIKE '%PH%' THEN 'Produk Hewan' WHEN id LIKE '%PM%' THEN 'Produk Makanan' END AS jenisproduk FROM hiday.PRODUK")
                desc = cursor.description
                nt_result = []
                for col in desc:
                    nt_result.append(col[0])
                # nt_result = namedtuple('Result', [col[0] for col in desc])
                nt_result.append("canDelete")

                resultAdmin = namedtuple('ResultAdmin',nt_result)

                result = []
                for row in cursor.fetchall():
                    if row[0] in idGabisaDelete:
                        result.append(resultAdmin(row[0],row[1],row[2],row[3],row[4],'False'))
                    else:
                        result.append(resultAdmin(row[0],row[1],row[2],row[3],row[4],'True'))

                print(result)

                temp = {}
                for i in range(len(result)):
                    temp[i+1] = result[i]
                    resultNum = list(temp.items())

                return render(request, 'list_produk.html', {"result" : resultNum, "role" : role})

            else:
                role = "pengguna"
                cursor.execute("SELECT id, nama, harga_jual, sifat_produk, CASE WHEN id LIKE '%HP%' THEN 'Hasil Panen' WHEN id LIKE '%PH%' THEN 'Produk Hewan' WHEN id LIKE '%PM%' THEN 'Produk Makanan' END AS jenisproduk FROM hiday.PRODUK")
                result = tupleFetch(cursor)
                temp = {}
                for i in range(len(result)):
                    temp[i+1] = result[i]
                    resultNum = list(temp.items())
                
                return render(request, 'list_produk.html', {"result" : resultNum, "role" : role})

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

   else:
        return HttpResponseRedirect('/login')

def buatProduk(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                form = BuatProduk(request.POST, request.FILES)

                if (form.is_valid and request.method == 'POST'):
                    idproduk = form.data.get("IdProduk")
                    nama = form.data.get("Nama")
                    hargajual = form.data.get("HargaJual")
                    sifat = form.data.get("SifatProduk")
                    checker = idproduk

                    # print(idproduk)
                    # print(nama)
                    # print(hargajual)
                    # print(sifat)
                    
                    cursor.execute("SET SEARCH_PATH TO HIDAY")
                    if (checker == "HP"):
                        cursor.execute("SELECT id FROM PRODUK WHERE id LIKE'HP%' ORDER BY id DESC LIMIT 1")
                    
                    elif (checker == "PH"):
                        cursor.execute("SELECT id FROM PRODUK WHERE id LIKE'PH%' ORDER BY id DESC LIMIT 1")

                    else:
                        cursor.execute("SELECT id FROM PRODUK WHERE id LIKE'PM%' ORDER BY id DESC LIMIT 1")
                    
                    result = cursor.fetchone()
                    cursor.execute("SET SEARCH_PATH TO public")

                    # print(result)
                    resultt = result[0]
                    resultt = resultt[2:]
                    # print(resultt)
                    idAngka = int(resultt) + 1
                    idproduk = "%s%03d" % (idproduk, idAngka)

                    cursor.execute("SET SEARCH_PATH TO HIDAY")
                    cursor.execute("INSERT INTO PRODUK VALUES ('" + idproduk + "', '" + nama + "', '" + hargajual + "', '" + sifat + "')")

                    if (checker == "HP"):
                        cursor.execute("INSERT INTO HASIL_PANEN VALUES ('" + idproduk + "')")

                    elif (checker == "PH"):
                        cursor.execute("INSERT INTO PRODUK_HEWAN VALUES ('" + idproduk + "')")

                    else:
                        cursor.execute("INSERT INTO PRODUK_MAKANAN VALUES ('" + idproduk + "')")

                    cursor.execute("SET SEARCH_PATH TO public")
                    cursor.close()
                    return HttpResponseRedirect('/crud-produk/list-produk')
                
                return render(request, 'buat_produk.html', {"form" : BuatProduk, "role" : role})

            else:
                role = "pengguna"
                return render(request, 'buat_produk.html', {"form" : BuatProduk, "role" : role})
            
        except Exception as e:
            print(e)            
        
    else:
        return HttpResponseRedirect('/login')

def ubahProduk(request, slug):
    if (request.session['role'] == ['admin']):
        role = "admin"
        form = UbahProduk(request.POST, request.FILES)
        cursor = connection.cursor()
        result = []

        cursor.execute("SET SEARCH_PATH TO HIDAY")
        cursor.execute("SELECT id, nama, harga_jual, sifat_produk, CASE WHEN id LIKE '%HP%' THEN 'Hasil Panen' WHEN id LIKE '%PH%' THEN 'Produk Hewan' WHEN id LIKE '%PM%' THEN 'Produk Makanan' END AS jenisproduk FROM PRODUK WHERE id = '" + ''.join(slug) + "'")
        result = cursor.fetchone()
        cursor.execute("SET SEARCH_PATH TO public")
        # print(result)

        context = {
            'id' : result[0],
            'nama' : result[1],
            'hargajual' : result[2],
            'sifat' : result[3],
            'jenisproduk' : result[4]
        }

        if (form.is_valid and request.method == 'POST'):
            hargajual = form.data.get("HargaJual")
            sifat = form.data.get("SifatProduk")

            cursor.execute("SET SEARCH_PATH TO HIDAY")
            cursor.execute("UPDATE PRODUK SET harga_jual = '" + hargajual + "', sifat_produk = '" + sifat + "' WHERE id = '" + ''.join(slug) + "'")
            cursor.execute("SET SEARCH_PATH TO public")
            cursor.close()

            return HttpResponseRedirect('/crud-produk/list-produk')
        
        return render(request, 'ubah_produk.html', {"form" : UbahProduk, "role" : role, "result" : context})

    else:
        role = "pengguna"
    
    return render(request, 'ubah_produk.html', {"form" : UbahProduk, "role" : role})

def deleteProduk(request, slug):
    if (request.session['role'] == ['admin']):
        role = "admin"
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO HIDAY")
        cursor.execute("DELETE FROM PRODUK WHERE id = '" + ''.join(slug) + "'")
        cursor.execute("SET SEARCH_PATH TO public")
        cursor.close()
    else:
        role = "pengguna"
    
    return HttpResponseRedirect('/crud-produk/list-produk')