from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from .forms import *

# def home(request):
#     return render(request, 'main/home.html')

def tupleFetch(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def index(request):
    cursor = connection.cursor()
    try:
        # cursor.execute("SET SEARCH_PATH TO HIDAY")
        cursor.execute("SELECT hiday.EMAIL FROM AKUN")
        result = tupleFetch(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'main/home.html', {'result': result})

def login(request):
    result = []
    FormLogin = LoginForm(request.POST)

    if (FormLogin.is_valid() and request.method == 'POST'):
        email = FormLogin.cleaned_data['email']
        password = FormLogin.cleaned_data['password']

        try:
            cursor = connection.cursor()
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            cursor.execute("SELECT * FROM AKUN WHERE Email ='" + email + "'")
            result = cursor.fetchone()

            if(result == None): 
                return HttpResponseNotFound("User Tidak Ditemukan")
            
            else:
                cursor.execute("SELECT * FROM ADMIN WHERE Email ='" + email + "'")
                cek_admin = cursor.fetchone()

                cursor.execute("SELECT * FROM PENGGUNA WHERE Email ='" + email + "'")
                cek_pengguna = cursor.fetchone()

                if(cek_admin != None):
                    role = "admin"
                    cursor.execute("SELECT * FROM ADMIN WHERE Email ='" + email + "' AND Password = '" + password + "'")
                    # result = cursor.fetchone()
                
                if(cek_pengguna != None):
                    role = "pengguna"
                    cursor.execute("SELECT * FROM PENGGUNA WHERE Email ='" + email + "' AND Password = '" + password + "'")
                    # result = cursor.fetchone()

                if (cursor.fetchone()):
                    cursor.execute("SET SEARCH_PATH TO public")
                    request.session['email'] = [email, password, result]
                    request.session['role'] = [role]
                
                else:
                    return HttpResponseNotFound("Login Gagal Cek Kembali Password")
            
        except Exception as e:
            print(e)
            cursor.close()

        finally:
            cursor.close()

        return HttpResponseRedirect('/profile')

    else:
        FormLogin = LoginForm()

    return render(request, 'login.html', {'form' : FormLogin})

def loggedInView(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        try:
            # cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM hiday.ADMIN WHERE EMAIL = '"+ request.session['email'][0] +"'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM hiday.PENGGUNA WHERE EMAIL = '"+ request.session['email'][0] +"'")
                result = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        return render(request, 'loginBerhasil.html', {"result" : result, "role" : role})

   else:
        return HttpResponseRedirect('/login')

def logout(request):
   try:
        del request.session['email']
   except:
        pass
   return HttpResponseRedirect('/login')

def isiLumbung(request):
   if request.session.has_key('email'):
        cursor = connection.cursor()
        result = []
        result2 = []
        result3 = []
        result4 = []
        role =''
        try:
            if (request.session['role'] == ['admin']):
                # cursor.execute("SET SEARCH_PATH TO HIDAY")
                cursor.execute("SELECT DISTINCT LM.id_lumbung, PR.id, PR.nama, PR.harga_jual, PR.sifat_produk, LM.jumlah FROM hiday.PRODUK PR, hiday.LUMBUNG_MEMILIKI_PRODUK LM, hiday.PRODUK_MAKANAN PM WHERE  LM.id_produk = PR.id AND PR.id = PM.id_produk")
                result = tupleFetch(cursor)
                cursor.execute("SELECT DISTINCT LM.id_lumbung, PR.id, PR.nama, PR.harga_jual, PR.sifat_produk, LM.jumlah FROM hiday.PRODUK PR, hiday.LUMBUNG_MEMILIKI_PRODUK LM, hiday.HASIL_PANEN HP WHERE  LM.id_produk = PR.id AND PR.id = HP.id_produk")
                result2 = tupleFetch(cursor)
                cursor.execute("SELECT DISTINCT LM.id_lumbung, PR.id, PR.nama, PR.harga_jual, PR.sifat_produk, LM.jumlah FROM hiday.PRODUK PR, hiday.LUMBUNG_MEMILIKI_PRODUK LM, hiday.PRODUK_HEWAN PH WHERE  LM.id_produk = PR.id AND PR.id = PH.id_produk")
                result3 = tupleFetch(cursor)
                role = "admin"

            else:
                email = str(request.session['email'][0])
                # cursor.execute("SET SEARCH_PATH TO HIDAY")
                cursor.execute("SELECT DISTINCT LM.id_lumbung, PR.id, PR.nama, PR.harga_jual, PR.sifat_produk, LM.jumlah FROM hiday.PRODUK PR, hiday.LUMBUNG_MEMILIKI_PRODUK LM, hiday.PRODUK_MAKANAN PM WHERE LM.id_produk = PR.id AND PR.id = PM.id_produk AND LM.id_lumbung = '" + ''.join(email) + "'")
                result = tupleFetch(cursor)
                cursor.execute("SELECT DISTINCT LM.id_lumbung, PR.id, PR.nama, PR.harga_jual, PR.sifat_produk, LM.jumlah FROM hiday.PRODUK PR, hiday.LUMBUNG_MEMILIKI_PRODUK LM, hiday.HASIL_PANEN HP WHERE LM.id_produk = PR.id AND PR.id = HP.id_produk AND LM.id_lumbung = '" + ''.join(email) + "'")
                result2 = tupleFetch(cursor)
                cursor.execute("SELECT DISTINCT LM.id_lumbung, PR.id, PR.nama, PR.harga_jual, PR.sifat_produk, LM.jumlah FROM hiday.PRODUK PR, hiday.LUMBUNG_MEMILIKI_PRODUK LM, hiday.PRODUK_HEWAN PH WHERE LM.id_produk = PR.id AND PR.id = PH.id_produk AND LM.id_lumbung = '" + ''.join(email) + "'")
                result3 = tupleFetch(cursor)
                cursor.execute("SELECT *  FROM LUMBUNG L WHERE L.email = '" + ''.join(email) + "'")
                result4 = tupleFetch(cursor)
                role = "pengguna"

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            temp = {}
            for i in range(len(result)):
                temp[i+1] = result[i]
            resultNum = list(temp.items())

            temp = {}
            for i in range(len(result2)):
                temp[i+1] = result2[i]
            resultNum2 = list(temp.items())

            temp = {}
            for i in range(len(result3)):
                temp[i+1] = result3[i]
            resultNum3 = list(temp.items())

        return render(request, 'isi_lumbung.html', {"result" : resultNum, "result2" : resultNum2, "result3" : resultNum3,"result4" : result4, "role" : role})

   else:
        return HttpResponseRedirect('/login')