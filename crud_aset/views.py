from django.shortcuts import render, redirect
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def listAset(request):
    if request.session.has_key('email'):
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"

            else:
                role = "pengguna"
        
        except Exception as e:
            print(e)
            
        return render(request, 'list_aset.html', {"role" : role})

    else:
        return HttpResponseRedirect('/login')

def listDekorasi(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.DEKORASI ON ID_Aset= ID")
                result = tupleFetch(cursor)

                cursor.execute("SELECT ID FROM hiday.ASET WHERE ID LIKE 'DK%' EXCEPT (SELECT ID_ASET FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET)")
                result2 = tupleFetch(cursor)

                role = "admin"

            else:
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.DEKORASI ON ID_Aset= ID")
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

        return render(request, 'list_dekorasi.html', {"result" : resultNum, "result2" : result2, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listBibitTanaman(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        result3 = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.BIBIT_TANAMAN ON ID_Aset= ID")
                result = tupleFetch(cursor)

                cursor.execute("SELECT ID FROM hiday.ASET WHERE ID LIKE 'BT%' EXCEPT (SELECT ID_ASET FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET)")
                result2 = tupleFetch(cursor)

                cursor.execute("SELECT ID_ASET FROM hiday.BIBIT_TANAMAN EXCEPT (SELECT ID_Bibit_Tanaman FROM hiday.BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN NATURAL JOIN hiday.HISTORI_TANAMAN)")
                result3 = tupleFetch(cursor)
    
                role = "admin"

            else:
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.BIBIT_TANAMAN ON ID_Aset= ID")
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

        return render(request, 'list_bibit_tanaman.html', {"result" : resultNum, "result2" : result2, "result3" : result3, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listKandang(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.KANDANG ON ID_Aset=ID")
                result = tupleFetch(cursor)

                cursor.execute("SELECT ID FROM hiday.ASET WHERE ID LIKE 'KD%' EXCEPT (SELECT ID_ASET FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET)")
                result2 = tupleFetch(cursor)

                role = "admin"

            else:
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.KANDANG ON ID_Aset=ID")
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

        return render(request, 'list_kandang.html', {"result" : resultNum, "result2" : result2, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listHewan(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        result3 = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT H.ID_Aset, nama, minimum_level, harga_beli, durasi_produksi, id_kandang FROM hiday.ASET A JOIN hiday.HEWAN H ON H.ID_Aset=A.ID JOIN hiday.KANDANG K ON H.ID_Kandang=K.ID_Aset")
                result = tupleFetch(cursor)

                cursor.execute("SELECT ID FROM hiday.ASET WHERE ID LIKE 'HW%' EXCEPT (SELECT ID_ASET FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET)")
                result2 = tupleFetch(cursor)

                cursor.execute("SELECT ID_ASET FROM hiday.HEWAN EXCEPT (SELECT ID_Hewan FROM hiday.HEWAN_MENGHASILKAN_PRODUK_HEWAN NATURAL JOIN hiday.HISTORI_HEWAN)")
                result3 = tupleFetch(cursor)

                role = "admin"

            else:
                cursor.execute("SELECT H.ID_Aset, nama, minimum_level, harga_beli, durasi_produksi, id_kandang FROM hiday.ASET A JOIN hiday.HEWAN H ON H.ID_Aset=A.ID JOIN hiday.KANDANG K ON H.ID_Kandang=K.ID_Aset")
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

        return render(request, 'list_hewan.html', {"result" : resultNum, "result2" : result2, "result3" : result3, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listAlatProduksi(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        result3 = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.ALAT_PRODUKSI ON ID_Aset=ID")
                result = tupleFetch(cursor)

                cursor.execute("SELECT ID FROM hiday.ASET WHERE ID LIKE 'AP%' EXCEPT (SELECT ID_ASET FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET)")
                result2 = tupleFetch(cursor)

                cursor.execute("SELECT ID_Aset FROM hiday.ALAT_PRODUKSI EXCEPT (SELECT ID_Alat_Produksi FROM hiday.PRODUKSI)")
                result3 = tupleFetch(cursor)

                role = "admin"

            else:
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.ALAT_PRODUKSI ON ID_Aset=ID")
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

        return render(request, 'list_alat_produksi.html', {"result" : resultNum, "result2" : result2, "result3" : result3, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def listPetakSawah(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.PETAK_SAWAH ON ID_Aset=ID")
                result = tupleFetch(cursor)

                cursor.execute("SELECT ID FROM hiday.ASET WHERE ID LIKE 'PS%' EXCEPT (SELECT ID_ASET FROM hiday.KOLEKSI_ASET_MEMILIKI_ASET)")
                result2 = tupleFetch(cursor)

                role = "admin"

            else:
                cursor.execute("SELECT * FROM hiday.ASET JOIN hiday.PETAK_SAWAH ON ID_Aset=ID")
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

        return render(request, 'list_petak_sawah.html', {"result" : resultNum, "result2" : result2, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def buatAset(request):
    if request.session.has_key('email'):
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"

            else:
                role = "pengguna"
        
        except Exception as e:
            print(e)
            
        return render(request, 'buat_aset.html', {"role" : role})

    else:
        return HttpResponseRedirect('/login')

def buatDekorasi(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT COUNT(*) FROM HIDAY.DEKORASI")
                result = cursor.fetchall()[0][0]

                if result < 9:
                    ID = "DK00" + str(result+1)
                elif result >= 99:
                    ID = "DK" + str(result+1)
                else:
                    ID = "DK0" + str(result+1)

                form = BuatDekorasi(initial={'ID' : ID})

                if (request.method == "POST"):
                    form = BuatDekorasi(data=request.POST)
                    if form.is_valid():
                        Nama = request.POST['Nama']
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        HargaJual = request.POST['HargaJual']
                        cursor.execute("INSERT INTO HIDAY.ASET VALUES(%s, %s, %s, %s)", [ID, Nama, MinimumLevel, HargaBeli])
                        cursor.execute("INSERT INTO HIDAY.DEKORASI VALUES(%s, %s)", [ID, HargaJual])

                        return redirect("/crud-aset/list-aset")
                    else:
                        return redirect("/crud-aset/buat-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_dekorasi.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def buatBibitTanaman(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT COUNT(*) FROM HIDAY.BIBIT_TANAMAN")
                result = cursor.fetchall()[0][0]

                if result < 9:
                    ID = "BT00" + str(result+1)
                elif result >= 99:
                    ID = "BT" + str(result+1)
                else:
                    ID = "BT0" + str(result+1)

                form = BuatBibitTanaman(initial={'ID' : ID})

                if (request.method == "POST"):
                    form = BuatBibitTanaman(data=request.POST)
                    if form.is_valid():
                        Nama = request.POST['Nama']
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        DurasiPanen = request.POST['DurasiPanen']
                        cursor.execute("INSERT INTO HIDAY.ASET VALUES(%s, %s, %s, %s)", [ID, Nama, MinimumLevel, HargaBeli])
                        cursor.execute("INSERT INTO HIDAY.BIBIT_TANAMAN VALUES(%s, %s)", [ID, DurasiPanen])

                        return redirect("/crud-aset/list-aset")
                    else:
                        return redirect("/crud-aset/buat-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_bibit_tanaman.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def buatKandang(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT COUNT(*) FROM HIDAY.KANDANG")
                result = cursor.fetchall()[0][0]

                if result < 9:
                    ID = "KD00" + str(result+1)
                elif result >= 99:
                    ID = "KD" + str(result+1)
                else:
                    ID = "KD0" + str(result+1)

                form = BuatKandang(initial={'ID' : ID})

                if (request.method == "POST"):
                    form = BuatKandang(data=request.POST)
                    if form.is_valid():
                        Nama = request.POST['Nama']
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        KapasitasMaks = request.POST['KapasitasMaks']
                        JenisHewan = request.POST['JenisHewan']
                        cursor.execute("INSERT INTO HIDAY.ASET VALUES(%s, %s, %s, %s)", [ID, Nama, MinimumLevel, HargaBeli])
                        cursor.execute("INSERT INTO HIDAY.KANDANG VALUES(%s, %s, %s)", [ID, KapasitasMaks, JenisHewan])

                        return redirect("/crud-aset/list-aset")
                    else:
                        return redirect("/crud-aset/buat-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_kandang.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def buatHewan(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        status_kandang = ""
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT COUNT(*) FROM HIDAY.HEWAN")
                result = cursor.fetchall()[0][0]

                if result < 9:
                    ID = "HW00" + str(result+1)
                elif result >= 99:
                    ID = "HW" + str(result+1)
                else:
                    ID = "HW0" + str(result+1)

                form = BuatHewan(initial={'ID' : ID})

                if (request.method == "POST"):
                    form = BuatHewan(data=request.POST)
                    if form.is_valid():
                        Nama = request.POST['Nama']
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        DurasiProduksi= request.POST['DurasiProduksi']
                        ID_Kandang = ""

                        cursor.execute("SELECT ID_Aset, jenis_hewan FROM HIDAY.KANDANG")
                        res = cursor.fetchall()
                        for i in range(len(res)):
                            if (res[i][1] == Nama):
                                ID_Kandang = res[i][0]

                        if (ID_Kandang == ""):
                            status_kandang = "unavailable"
                        else:
                            cursor.execute("INSERT INTO HIDAY.ASET VALUES(%s, %s, %s, %s)", [ID, Nama, MinimumLevel, HargaBeli])
                            cursor.execute("INSERT INTO HIDAY.HEWAN VALUES(%s, %s, %s)", [ID, DurasiProduksi, ID_Kandang])

                            return redirect("/crud-aset/list-aset")
                    else:
                        return redirect("/crud-aset/buat-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_hewan.html', {"ID" : ID, "form" : form, "status_kandang" : status_kandang, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def buatAlatProduksi(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT COUNT(*) FROM HIDAY.ALAT_PRODUKSI")
                result = cursor.fetchall()[0][0]

                if result < 9:
                    ID = "AP00" + str(result+1)
                elif result >= 99:
                    ID = "AP" + str(result+1)
                else:
                    ID = "AP0" + str(result+1)

                form = BuatAlatProduksi(initial={'ID' : ID})

                if (request.method == "POST"):
                    form = BuatAlatProduksi(data=request.POST)
                    if form.is_valid():
                        Nama = request.POST['Nama']
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        KapasitasMaks = request.POST['KapasitasMaks']
                        cursor.execute("INSERT INTO HIDAY.ASET VALUES(%s, %s, %s, %s)", [ID, Nama, MinimumLevel, HargaBeli])
                        cursor.execute("INSERT INTO HIDAY.ALAT_PRODUKSI VALUES(%s, %s)", [ID, KapasitasMaks])

                        return redirect("/crud-aset/list-aset")
                    else:
                        return redirect("/crud-aset/buat-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_alat_produksi.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def buatPetakSawah(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT COUNT(*) FROM HIDAY.PETAK_SAWAH")
                result = cursor.fetchall()[0][0]

                if result < 9:
                    ID = "PS00" + str(result+1)
                elif result >= 99:
                    ID = "PS" + str(result+1)
                else:
                    ID = "PS0" + str(result+1)

                form = BuatPetakSawah(initial={'ID' : ID})

                cursor.execute("SELECT nama FROM hiday.ASET JOIN hiday.BIBIT_TANAMAN ON ID_Aset= ID")
                Jenis_Tanaman = cursor.fetchall()

                if (request.method == "POST"):
                    form = BuatPetakSawah(data=request.POST)
                    if form.is_valid():
                        Nama = request.POST['Nama']
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        JenisTanaman = request.POST['JenisTanaman']
                        cursor.execute("INSERT INTO HIDAY.ASET VALUES(%s, %s, %s, %s)", [ID, Nama, MinimumLevel, HargaBeli])
                        cursor.execute("INSERT INTO HIDAY.PETAK_SAWAH VALUES(%s, %s)", [ID, JenisTanaman])

                        return redirect("/crud-aset/list-aset")
                    else:
                        return redirect("/crud-aset/buat-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_petak_sawah.html', {"ID" : ID, "JenisTanaman" : Jenis_Tanaman, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def ubahDekorasi(request, key):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        form = UbahDekorasi()
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT * FROM HIDAY.ASET JOIN HIDAY.DEKORASI ON ID_Aset=ID WHERE ID_Aset=%s", [key])
                result = cursor.fetchall()[0]

                initial_data = {
                    'ID' : result[0],
                    'Nama' : result[1],
                    'MinimumLevel' : result[2],
                    'HargaBeli' : result[3],
                    'HargaJual' : result[5]
                }
                form = UbahDekorasi(initial=initial_data)

                if (request.method == "POST"):
                    form = UbahDekorasi(data=request.POST)
                    if form.is_valid():
                        ID = result[0]
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        HargaJual = request.POST['HargaJual']
                        cursor.execute("UPDATE HIDAY.ASET SET minimum_level = %s, harga_beli =%s WHERE id = %s", [MinimumLevel, HargaBeli, ID])
                        cursor.execute("UPDATE HIDAY.DEKORASI SET harga_jual = %s WHERE id_aset = %s", [HargaJual, ID])

                        return redirect("/crud-aset/list-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_dekorasi.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def ubahBibitTanaman(request, key):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        form = UbahBibitTanaman()
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT * FROM HIDAY.ASET JOIN HIDAY.BIBIT_TANAMAN ON ID_Aset=ID WHERE ID_Aset=%s", [key])
                result = cursor.fetchall()[0]

                initial_data = {
                    'ID' : result[0],
                    'Nama' : result[1],
                    'MinimumLevel' : result[2],
                    'HargaBeli' : result[3],
                    'DurasiPanen' : result[5]
                }
                form = UbahBibitTanaman(initial=initial_data)

                if (request.method == "POST"):
                    form = UbahBibitTanaman(data=request.POST)
                    if form.is_valid():
                        ID = result[0]
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        DurasiPanen = request.POST['DurasiPanen']
                        cursor.execute("UPDATE HIDAY.ASET SET minimum_level = %s, harga_beli =%s WHERE id = %s", [MinimumLevel, HargaBeli, ID])
                        cursor.execute("UPDATE HIDAY.BIBIT_TANAMAN SET durasi_panen = %s WHERE id_aset = %s", [DurasiPanen, ID])

                        return redirect("/crud-aset/list-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_bibit_tanaman.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def ubahKandang(request, key):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        form = UbahKandang()
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT * FROM HIDAY.ASET JOIN HIDAY.KANDANG ON ID_Aset=ID WHERE ID_Aset=%s", [key])
                result = cursor.fetchall()[0]

                initial_data = {
                    'ID' : result[0],
                    'Nama' : result[1],
                    'MinimumLevel' : result[2],
                    'HargaBeli' : result[3],
                    'KapasitasMaks' : result[5],
                    'JenisHewan' : result[6]
                }
                form = UbahKandang(initial=initial_data)

                if (request.method == "POST"):
                    form = UbahKandang(data=request.POST)
                    if form.is_valid():
                        ID = result[0]
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        KapasitasMaks = request.POST['KapasitasMaks']
                        cursor.execute("UPDATE HIDAY.ASET SET minimum_level = %s, harga_beli =%s WHERE id = %s", [MinimumLevel, HargaBeli, ID])
                        cursor.execute("UPDATE HIDAY.KANDANG SET kapasitas_maks = %s WHERE id_aset = %s", [KapasitasMaks, ID])

                        return redirect("/crud-aset/list-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_kandang.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def ubahHewan(request, key):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        form = UbahHewan()
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT * FROM HIDAY.ASET JOIN HIDAY.HEWAN ON ID_Aset=ID WHERE ID_Aset=%s", [key])
                result = cursor.fetchall()[0]

                initial_data = {
                    'ID' : result[0],
                    'Nama' : result[1],
                    'MinimumLevel' : result[2],
                    'HargaBeli' : result[3],
                    'DurasiProduksi' : result[5],
                    'IDKandang' : result[6]
                }
                form = UbahHewan(initial=initial_data)

                if (request.method == "POST"):
                    form = UbahHewan(data=request.POST)
                    if form.is_valid():
                        ID = result[0]
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        DurasiProduksi = request.POST['DurasiProduksi']
                        cursor.execute("UPDATE HIDAY.ASET SET minimum_level = %s, harga_beli =%s WHERE id = %s", [MinimumLevel, HargaBeli, ID])
                        cursor.execute("UPDATE HIDAY.HEWAN SET durasi_produksi = %s WHERE id_aset = %s", [DurasiProduksi, ID])

                        return redirect("/crud-aset/list-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_hewan.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')


def ubahAlatProduksi(request, key):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        form = UbahAlatProduksi()
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT * FROM HIDAY.ASET JOIN HIDAY.ALAT_PRODUKSI ON ID_Aset=ID WHERE ID_Aset=%s", [key])
                result = cursor.fetchall()[0]

                initial_data = {
                    'ID' : result[0],
                    'Nama' : result[1],
                    'MinimumLevel' : result[2],
                    'HargaBeli' : result[3],
                    'KapasitasMaks' : result[5],
                }
                form = UbahAlatProduksi(initial=initial_data)

                if (request.method == "POST"):
                    form = UbahAlatProduksi(data=request.POST)
                    if form.is_valid():
                        ID = result[0]
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        KapasitasMaks = request.POST['KapasitasMaks']
                        cursor.execute("UPDATE HIDAY.ASET SET minimum_level = %s, harga_beli =%s WHERE id = %s", [MinimumLevel, HargaBeli, ID])
                        cursor.execute("UPDATE HIDAY.ALAT_PRODUKSI SET kapasitas_maks = %s WHERE id_aset = %s", [KapasitasMaks, ID])

                        return redirect("/crud-aset/list-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_alat_produksi.html', {"ID" : ID, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def ubahPetakSawah(request, key):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        ID = ""
        form = UbahPetakSawah()
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
                cursor.execute("SELECT * FROM HIDAY.ASET JOIN HIDAY.PETAK_SAWAH ON ID_Aset=ID WHERE ID_Aset=%s", [key])
                result = cursor.fetchall()[0]

                initial_data = {
                    'ID' : result[0],
                    'Nama' : result[1],
                    'MinimumLevel' : result[2],
                    'HargaBeli' : result[3],
                }

                form = UbahPetakSawah(initial=initial_data)

                cursor.execute("SELECT nama FROM hiday.ASET JOIN hiday.BIBIT_TANAMAN ON ID_Aset= ID")
                Jenis_Tanaman = cursor.fetchall()

                if (request.method == "POST"):
                    form = UbahPetakSawah(data=request.POST)
                    if form.is_valid():
                        ID = result[0]
                        MinimumLevel = request.POST['MinimumLevel']
                        HargaBeli = request.POST['HargaBeli']
                        JenisTanaman = request.POST['JenisTanaman']
                        cursor.execute("UPDATE HIDAY.ASET SET minimum_level = %s, harga_beli =%s WHERE id = %s", [MinimumLevel, HargaBeli, ID])
                        cursor.execute("UPDATE HIDAY.PETAK_SAWAH SET jenis_tanaman = %s WHERE id_aset = %s", [JenisTanaman, ID])

                        return redirect("/crud-aset/list-aset")

            else:
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_petak_sawah.html', {"ID" : ID, "JenisTanaman" : Jenis_Tanaman, "form" : form, "role" : role})

    else:
        return HttpResponseRedirect('/login')


def hapusAset(request, key):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        try:
            if (request.session['role'] == ['admin']):
                cursor.execute("DELETE FROM HIDAY.ASET WHERE id = %s", [key])
                return redirect("/crud-aset/list-aset")

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

    else:
        return HttpResponseRedirect('/login')
