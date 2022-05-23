from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listKoleksiAset(request):
    if request.session.has_key('email'):
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"

            else:
                role = "pengguna"
        
        except Exception as e:
            print(e)
            
        return render(request, 'list_koleksi_aset.html', {"role" : role})

    else:
        return HttpResponseRedirect('/login')

def listKoleksiAsetDekorasi(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'DK%'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'DK%'")
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

        return render(request, 'list_koleksi_aset_dekorasi.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def listKoleksiAsetBibitTanaman(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'BT%'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'BT%'")
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

        return render(request, 'list_koleksi_aset_bibit_tanaman.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def listKoleksiAsetKandang(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'KD%'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'KD%'")
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

        return render(request, 'list_koleksi_aset_kandang.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def listKoleksiAsetHewan(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'HW%'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'HW%'")
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

        return render(request, 'list_koleksi_aset_hewan.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def listKoleksiAsetAlatProduksi(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'AP%'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'AP%'")
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

        return render(request, 'list_koleksi_aset_alat_produksi.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def listKoleksiAsetPetakSawah(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'PS%'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM HIDAY.KOLEKSI_ASET_MEMILIKI_ASET JOIN HIDAY.ASET ON ID_Aset=ID JOIN HIDAY.KOLEKSI_ASET ON ID_Koleksi_Aset=Email WHERE ID_Aset LIKE 'PS%'")
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

        return render(request, 'list_koleksi_aset_petak_sawah.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')