from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *
from main.forms import LoginForm
import datetime

# Create your views here.

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listTransaksiPaketKoin(request):

    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        role = ''
        
        try:
            if (request.session['role'] == ['admin']):                
                cursor.execute("SELECT * FROM hiday.TRANSAKSI_PEMBELIAN_KOIN")
                result = tupleFetch(cursor)
                role = "admin"


            else:
                email = request.session['email'][0]
                cursor.execute("SELECT * FROM hiday.TRANSAKSI_PEMBELIAN_KOIN WHERE email='" + email + "'")
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

        return render(request, 'list_transaksi_paket_koin.html', {"result" : resultNum, "role" : role})

    else:
        return HttpResponseRedirect('/login')

def formPaketKoin(request, slug):
    if (request.session['role'] == ['pengguna']):
        role = "pengguna"
        # print('uuu')
        form = FormPaketKoin(request.POST, request.FILES)
        cursor = connection.cursor()
        result = []

        cursor.execute("SELECT * FROM hiday.PAKET_KOIN WHERE jumlah_koin="+ str(slug)+ ";")
        result = cursor.fetchone()

        print('aaa')

        context = {
            'jumlah_koin' : result[0],
            'harga' : result[1]
        }

        if (form.is_valid and request.method == 'POST'):
            paket_koin = int(context['jumlah_koin'])
            
            # form.data.get('PaketKoin')
            harga = int(context['harga'])
            # form.data.get('Harga')
            # print(paket_koin)
            # print(harga)
            jumlah = form.data.get('Jumlah')
            # print(jumlah)
            caraPembayaran = form.data.get('CaraPembayaran')
            email = request.session['email'][0]
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total_biaya = harga*int(jumlah)
            

            try:
                print('bisa')
                cursor.execute("INSERT INTO hiday.TRANSAKSI_PEMBELIAN_KOIN VALUES('"+ email+"', '"+dt+"',"+str(jumlah)+", '"+ str(caraPembayaran)+ "', "+str(paket_koin)+ ", "+ str(total_biaya) +");")
            
            except Exception as e:
                print(e)
                cursor.close()

            finally:
                cursor.close()
            return HttpResponseRedirect('/cr-transaksi-pembelian-koin/list-transaksi-paket-koin')

        return render(request, 'form_paket_koin.html', {'form' : FormPaketKoin, "role" : role, "result" : context})
    
    else:
        role = "admin"

    return render(request, 'form_paket_koin.html', {'form' : FormPaketKoin, "role" : role})


