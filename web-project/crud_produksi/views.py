from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listProduksi(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        resultt = []
        role =''
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                 # cursor.execute("SET SEARCH_PATH TO HIDAY")
                cursor.execute("SELECT P.id_alat_produksi FROM hiday.PRODUKSI AS P, hiday.HISTORI_PRODUKSI_MAKANAN AS HP WHERE P.id_alat_produksi = HP.id_alat_produksi AND P.id_produk_makanan = HP.id_produk_makanan")
                resultt = tupleFetch(cursor)

                idGabisaDelete = []
                for i in range(len(resultt)):
                    idGabisaDelete.append(resultt[i][0])

                cursor.execute("SELECT P.id_produk_makanan FROM hiday.PRODUKSI AS P, hiday.HISTORI_PRODUKSI_MAKANAN AS HP WHERE P.id_alat_produksi = HP.id_alat_produksi AND P.id_produk_makanan = HP.id_produk_makanan")
                resultt = tupleFetch(cursor)

                idMakananGabisaDelete = []
                for i in range(len(resultt)):
                    idMakananGabisaDelete.append(resultt[i][0])

                cursor.execute("SELECT PRO.nama AS nama, A.nama AS namaAset, durasi, jumlah_unit_hasil, PRO.id, P.id_alat_produksi FROM hiday.PRODUKSI P JOIN hiday.ASET A ON P.Id_alat_produksi = A.id JOIN hiday.PRODUK PRO ON P.Id_produk_makanan = PRO.id")
                desc = cursor.description
                nt_result = []
                for col in desc:
                    nt_result.append(col[0])

                nt_result.append("canDelete")
                resultAdmin = namedtuple('ResultAdmin',nt_result)

                result = []
                for row in cursor.fetchall():
                    if (row[5] in idGabisaDelete) and (row[4] in idMakananGabisaDelete):
                        result.append(resultAdmin(row[0],row[1],row[2],row[3],row[4],row[5],'False'))
                    else:
                        result.append(resultAdmin(row[0],row[1],row[2],row[3],row[4],row[5],'True'))
                                
                temp = {}
                resultNum = []
                for i in range(len(result)):
                    temp[i+1] = result[i]
                    resultNum = list(temp.items())
                
                return render(request, 'list_produksi.html', {"result" : resultNum, "role" : role})

            else:
                role = "pengguna"
                cursor.execute("SELECT PRO.nama AS nama, A.nama AS namaAset, durasi, jumlah_unit_hasil, PRO.id FROM hiday.PRODUKSI P JOIN hiday.ASET A ON P.Id_alat_produksi = A.id JOIN hiday.PRODUK PRO ON P.Id_produk_makanan = PRO.id")
                result = tupleFetch(cursor)

                temp = {}
                for i in range(len(result)):
                    temp[i+1] = result[i]
                    resultNum = list(temp.items())

                return render(request, 'list_produksi.html', {"result" : resultNum, "role" : role})

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
   else:
        return HttpResponseRedirect('/login')

def buatProduksi(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        resultPM = []
        resultAlat = []
        resultBahan = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                # form = BuatProduksi(request.POST, request.FILES)
                # formBahan = BahanProduksi(request.POST, request.FILES)

                # BahanFormSet = formset_factory(BahanProduksi, extra=0) 

                # cursor.execute("SET SEARCH_PATH TO HIDAY")
                cursor.execute("SELECT id_produk, nama FROM hiday.PRODUK_MAKANAN, hiday.PRODUK WHERE id = id_produk")
                resultPM = tupleFetch(cursor)

                cursor.execute("SELECT id, nama FROM hiday.ASET, hiday.ALAT_PRODUKSI WHERE id = id_aset")
                resultAlat = tupleFetch(cursor)

                cursor.execute("SELECT id, nama FROM hiday.PRODUK")
                resultBahan = tupleFetch(cursor)

                # if (form.is_valid and formBahan.is_valid and request.method == 'POST'):
                if (request.method == 'POST'):
                    # idproduk = form.data.get("IdProduk")
                    # idalat = form.data.get("IdAlat")
                    # durasi = form.data.get("Durasi")
                    # jumlah = form.data.get("Jumlah")

                    idproduk = request.POST['IdProduk']
                    idalat = request.POST['IdAlat']
                    durasi = request.POST['Durasi']
                    jumlah = request.POST['Jumlah']
                    idbahan = request.POST['ID']
                    jumlahbahan = request.POST['J1']

                    durasi = "00:" + durasi + ":00"

                    print(idproduk)
                    print(idalat)
                    print(durasi)
                    print(jumlah)
                    print(idbahan)
                    print(jumlahbahan)
                    
                    # cursor.execute("SET SEARCH_PATH TO HIDAY")
                    cursor.execute("INSERT INTO hiday.PRODUKSI VALUES ('" + idalat + "', '" + idproduk + "', '" + durasi + "', '" + jumlah + "')")
                    cursor.execute("INSERT INTO hiday.PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN VALUES ('" + idproduk + "', '" + idbahan + "', '" + jumlahbahan + "')")

                    # cursor.execute("SET SEARCH_PATH TO public")
                    cursor.close()
                    return HttpResponseRedirect('/crud-produksi/list-produksi')
                
                return render(request, 'buat_produksi.html', {"form" : BuatProduksi, "role" : role, "DataProduk" : resultPM, "DataAset" : resultAlat, "DataBahan" : resultBahan})

            else:
                role = "pengguna"
                return render(request, 'buat_produksi.html', {"form" : BuatProduksi, "role" : role})
            
        except Exception as e:
            print(e)            
        
    else:
        return HttpResponseRedirect('/login')

def detailProduksi(request, slug):
    cursor = connection.cursor()
    result = []
    result2 = []
    # cursor.execute("SET SEARCH_PATH TO HIDAY")
    cursor.execute("SELECT PRO.nama AS nama, A.nama AS namaAset, durasi, jumlah_unit_hasil, PRO.id FROM hiday.PRODUKSI P JOIN hiday.ASET A ON P.Id_alat_produksi = A.id JOIN hiday.PRODUK PRO ON P.Id_produk_makanan = PRO.id WHERE PRO.id = '" + ''.join(slug) + "'")
    result = cursor.fetchone()
    id_produk = result[4]
    print(result[4])

    cursor.execute("SELECT Id_produk_makanan, P.nama as Bahan, Jumlah FROM hiday.PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN PD, hiday.PRODUK P WHERE PD.id_produk = P.id AND PD.id_produk_makanan = '" + ''.join(id_produk) + "'")
    result2 = tupleFetch(cursor)

    cursor.close()
    temp = {}
    for i in range(len(result2)):
        temp[i+1] = result2[i]
    resultNum = list(temp.items())

    context = {
        'nama' : result[0],
        'namaaset' : result[1],
        'durasi' : result[2],
        'jumlah_unit_hasil' : result[3]
    }

    return render(request, "detail_produksi.html", {"result2": resultNum, "res": context})

def ubahProduksi(request, slug):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                form = UbahProduksi(request.POST, request.FILES)

                cursor.execute("SELECT PRO.nama AS nama, A.nama AS namaAset, durasi, jumlah_unit_hasil, PRO.id as idproduk, P.Id_alat_produksi as idalat FROM hiday.PRODUKSI P JOIN hiday.ASET A ON P.Id_alat_produksi = A.id JOIN hiday.PRODUK PRO ON P.Id_produk_makanan = PRO.id WHERE PRO.id = '" + ''.join(slug) + "'")
                result = cursor.fetchone()
                id_produk = result[4]

                cursor.execute("SELECT Id_produk_makanan, P.nama as Bahan, Jumlah FROM hiday.PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN PD, hiday.PRODUK P WHERE PD.id_produk = P.id AND PD.id_produk_makanan = '" + ''.join(id_produk) + "'")
                result2 = tupleFetch(cursor)

                temp = {}
                for i in range(len(result2)):
                    temp[i+1] = result2[i]
                resultNum = list(temp.items())

                context = {
                    'nama' : result[0],
                    'namaaset' : result[1],
                    'durasi' : int(str(result[2])[3:5]),
                    'jumlah_unit_hasil' : result[3],
                    'idproduk' : result[4],
                    'idalat' : result[5]
                }

                if (form.is_valid and request.method == 'POST'):
                    idpro = form.data.get("IdProduk")
                    idal = form.data.get("IdAlat")
                    durasi = form.data.get("Durasi")
                    jumlah = form.data.get("Jumlah")

                    durasi = "00:" + durasi + ":00"

                    print(idpro)
                    print(idal)
                    print(durasi)
                    print(jumlah)
                    
                    # cursor.execute("SET SEARCH_PATH TO HIDAY")
                    cursor.execute("UPDATE hiday.PRODUKSI SET durasi = '" + durasi + "', jumlah_unit_hasil = '" + jumlah + "' WHERE id_produk_makanan = '" + idpro + "' AND id_alat_produksi = '" + idal + "'")

                    # cursor.execute("SET SEARCH_PATH TO public")
                    cursor.close()
                    return HttpResponseRedirect('/crud-produksi/list-produksi')
                
                return render(request, 'ubah_produksi.html', {"form" : BuatProduksi, "role" : role, "result2": resultNum, "res": context})

            else:
                role = "pengguna"
                return render(request, 'ubah_produksi.html', {"form" : BuatProduksi, "role" : role})
            
        except Exception as e:
            print(e)            
        
    else:
        return HttpResponseRedirect('/login')
    
def deleteProduksi(request, slug):
    if (request.session['role'] == ['admin']):
        role = "admin"
        cursor = connection.cursor()
        # cursor.execute("SET SEARCH_PATH TO HIDAY")
        cursor.execute("DELETE FROM hiday.PRODUKSI WHERE id_produk_makanan = '" + ''.join(slug) + "'")
        # cursor.execute("SET SEARCH_PATH TO public")
        cursor.close()
    else:
        role = "pengguna"
    
    return HttpResponseRedirect('/crud-produksi/list-produksi')