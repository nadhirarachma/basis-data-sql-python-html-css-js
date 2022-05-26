from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

def tuple_fetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def list_histori_pesanan(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result0 = []
        result = []
        result2 = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
            else:
                role = "pengguna"
            
            cursor.execute("SELECT * FROM hiday.PESANAN order by id ASC;")
            result0 = tuple_fetch(cursor)
            cursor.execute("SELECT * FROM hiday.PESANAN where id not in (select id_pesanan from hiday.histori_penjualan) order by id ASC;")
            result = tuple_fetch(cursor)
            cursor.execute("SELECT * FROM hiday.PESANAN where id in (select id_pesanan from hiday.histori_penjualan) order by id ASC;")
            result2 = tuple_fetch(cursor)

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'list_histori_pesanan.html', {"result0" : result0, "result" : result, "result2" : result2, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def view_detail_pesanan(request, id):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result1 = []
        result2 = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
            else:
                role = "pengguna"

            cursor.execute("SELECT id, nama, jenis, total, status FROM hiday.pesanan WHERE id = '" + id +"';")
            result1 = tuple_fetch(cursor)
            cursor.execute("SELECT p.nama, dp.jumlah, dp.subtotal FROM hiday.detail_pesanan dp JOIN hiday.produk p on dp.id_produk = p.id WHERE dp.id_pesanan = '" + id +"';")
            result2 = tuple_fetch(cursor)

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'detail_pesanan.html', {"result1" : result1, "result2" : result2, "role" : role, "id" : id})

    else:
        return HttpResponseRedirect('/login')

def buat_pesanan(request):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        id_new_pesanan = ""
        list_produk = []
        try:
            if (request.session['role'] == ['admin']):
                role = "admin"
            else:
                role = "pengguna"

            cursor.execute("select id from hiday.pesanan order by id DESC limit 1")
            int_new_pesanan = int(tuple_fetch(cursor)[0][0].split("S")[1].lstrip('0')) + 1
            id_new_pesanan = "PS"
            for i in range(0, 3 - len(str(int_new_pesanan))):
                id_new_pesanan = id_new_pesanan + "0"
            id_new_pesanan = id_new_pesanan + str(int_new_pesanan)
            cursor.execute("select * from hiday.produk")
            list_produk = tuple_fetch(cursor)

            if request.method == 'POST':
                res_dict = request.POST.dict()
                cursor.execute("insert into hiday.pesanan values('" + id_new_pesanan + "', 'Baru Dipesan', '" + res_dict["jenis_pesanan"] + "', '" + res_dict["nama_pesanan"] + "', 0)")
                
                res_dict.pop("csrfmiddlewaretoken")
                res_dict.pop("nama_pesanan")
                res_dict.pop("jenis_pesanan")

                no_urut = 1
                for i in res_dict:
                    if int(res_dict.get(i)) > 0:
                        cursor.execute("select harga_jual from hiday.produk where id = '" + i + "'")
                        res = tuple_fetch(cursor)
                        harga_jual = int(res[0][0])
                        subtotal = harga_jual*int(res_dict.get(i))
                        cursor.execute("insert into hiday.detail_pesanan values('" + id_new_pesanan + "', " + str(no_urut) + ", " + str(subtotal) + ", " + str(res_dict.get(i)) + ", '" + i + "')")
                        no_urut = no_urut + 1

                return HttpResponseRedirect('/crud-pesanan/list-histori-pesanan')

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'buat_pesanan.html', {"role" : role, "id_new_pesanan" : id_new_pesanan, "list_produk" : list_produk})

    else:
        return HttpResponseRedirect('/login')

def ubah_pesanan(request, id):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result1 = []
        result2 = []
        try:
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT id, nama, jenis, total, status FROM hiday.pesanan WHERE id = '" + id +"';")
                result1 = tuple_fetch(cursor)
                cursor.execute("SELECT p.nama, dp.jumlah, dp.subtotal FROM hiday.detail_pesanan dp JOIN hiday.produk p on dp.id_produk = p.id WHERE dp.id_pesanan = '" + id +"';")
                result2 = tuple_fetch(cursor)

            if request.method == 'POST':
                nama_pesanan = request.POST["nama_pesanan"]
                jenis_pesanan = request.POST["jenis_pesanan"]
                status_pesanan = request.POST["status_pesanan"]

                cursor.execute("update hiday.pesanan set nama = '" + nama_pesanan + "', jenis = '" + jenis_pesanan + "', status = '" + status_pesanan + "' where id = '" + id + "'")
                return HttpResponseRedirect('/crud-pesanan/list-histori-pesanan')

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'ubah_pesanan.html', {"result1" : result1, "result2" : result2})

    else:
        return HttpResponseRedirect('/login')

def hapus_pesanan(request, id):
    if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            if (request.session['role'] == ['admin']):
                cursor.execute("delete from hiday.pesanan where id = '" + id + "'")

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return HttpResponseRedirect('/crud-pesanan/list-histori-pesanan')

    else:
        return HttpResponseRedirect('/login')

