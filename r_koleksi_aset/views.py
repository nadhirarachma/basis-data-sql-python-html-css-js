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
        cursor = connection.cursor()
        result = []
        try:
            cursor.execute("SET SEARCH_PATH TO HIDAY")
            if (request.session['role'] == ['admin']):
                cursor.execute("SELECT * FROM KOLEKSI_ASET_MEMILIKI_ASET JOIN ASET ON ID_Aset=ID JOIN KOLEKSI_ASET ON ID_Koleksi_Aset=Email")
                result = tupleFetch(cursor)
                role = "admin"

            else:
                cursor.execute("SELECT * FROM KOLEKSI_ASET_MEMILIKI_ASET JOIN ASET ON ID_Aset=ID JOIN KOLEKSI_ASET ON ID_Koleksi_Aset=Email")
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

        return render(request, 'list_koleksi_aset.html', {"result" : resultNum, "role" : role})

   else:
        return HttpResponseRedirect('/login')