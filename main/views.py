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
        cursor.execute("SET SEARCH_PATH TO HIDAY")
        cursor.execute("SELECT EMAIL FROM AKUN")
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
            # cursor.execute("SELECT * FROM ADMIN AS ADM WHERE ADM.Email ='" + email + "' AND ADM.Password = '" + password + "'")
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
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM ADMIN WHERE EMAIL = '"+ request.session['email'][0] +"'")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM PENGGUNA WHERE EMAIL = '"+ request.session['email'][0] +"'")
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