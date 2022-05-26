from ntpath import join
import re
from unittest import result
from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

# Create your views here.

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listPaketKoin(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        bisaDelete = []

        try:
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.PAKET_KOIN")
                result = tupleFetch(cursor)
                role = "admin"
                cursor.execute("SELECT jumlah_koin FROM hiday.PAKET_KOIN WHERE jumlah_koin NOT IN (SELECT paket_koin FROM hiday.TRANSAKSI_PEMBELIAN_KOIN);")
                bisaDelete = tupleFetch(cursor)

                coba = []

                if (len(bisaDelete)>0):
                    for i in (bisaDelete):
                        for j in (result):
                            if(j.jumlah_koin == i.jumlah_koin):
                                coba.append(j.jumlah_koin)
            
            
            else:
                cursor.execute("SELECT * FROM hiday.PAKET_KOIN")
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
            # print(resultNum)

        return render(request, 'list_paket_koin.html', {"result" : resultNum, "role" : role, "coba":coba})

   else:
        return HttpResponseRedirect('/login')

def buatPaketKoin(request):
    role = ''
    formBuatPaket = BuatPaketKoin(request.POST)
  
    if (request.session['role'] == ['admin']):
        role = "admin"

    else:
        role = "pengguna"

    if (formBuatPaket.is_valid() and request.method == 'POST'):
        jumlahKoin = formBuatPaket.cleaned_data['JumlahKoin']
        harga = formBuatPaket.cleaned_data['Harga']

        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO hiday.PAKET_KOIN VALUES("+ str(jumlahKoin) +"," + str(harga)+ ");")
            
        except Exception as e:
            print(e)
            cursor.close()

        finally:
            cursor.close()

        return HttpResponseRedirect('/crud-paket-koin/list-paket-koin')

    else:        
        formBuatPaket = BuatPaketKoin()

    return render(request, 'create_paket_koin.html', {'form' : BuatPaketKoin, "role" : role})

    

def updatePaketKoin(request, slug):
    if (request.session['role'] == ['admin']):
        role = "admin"
        form = UpdatePaketKoin(request.POST, request.FILES)
        cursor = connection.cursor()
        result = []

        cursor.execute("SELECT * FROM hiday.PAKET_KOIN WHERE jumlah_koin="+ str(slug)+ ";")
        result = cursor.fetchone()

        context = {
            'jumlah_koin' : result[0],
            'harga' : result[1]
        }

        if (form.is_valid and request.method == 'POST'):
            # jumlahkoin = form.data.get('JumlahKoin')
            harga = form.data.get('Harga')

            try:
                cursor.execute('UPDATE hiday.PAKET_KOIN SET harga='+ harga +'WHERE jumlah_koin ='+ "".join(slug)+';')
            
            except Exception as e:
                print(e)
                cursor.close()

            finally:
                cursor.close()
            return HttpResponseRedirect('/crud-paket-koin/list-paket-koin')

        return render(request, 'update_paket_koin.html', {'form' : UpdatePaketKoin, "role" : role, "result" : context})
    
    else:
        role = "pengguna"

    return render(request, 'update_paket_koin.html', {'form' : UpdatePaketKoin, "role" : role})

def deletePaketKoin(request, slug):
    if (request.session['role'] == ['admin']):
        role = "admin"
        form = DeletePaketKoin(request.POST, request.FILES)
        cursor = connection.cursor()
        
        result = []

        cursor.execute("SELECT * FROM hiday.PAKET_KOIN WHERE jumlah_koin="+ str(slug)+ ";")
        result = cursor.fetchone()

        context = {
            'jumlah_koin' : result[0],
            'harga' : result[1]
        }

       
        if (form.is_valid and request.method == 'POST'):
            try:
                cursor.execute("DELETE FROM hiday.PAKET_KOIN WHERE jumlah_koin ="+ "".join(slug)+";")
            
            except Exception as e:
                print(e)
                cursor.close()

            finally:
                cursor.close()
            return HttpResponseRedirect('/crud-paket-koin/list-paket-koin')

        return render(request, 'form_delete_paket_koin.html', {'form' : DeletePaketKoin, "role" : role, "result" : context})
    
    else:
        role = "pengguna"

    return render(request, 'form_delete_paket_koin.html', {'form' : DeletePaketKoin, "role" : role})
