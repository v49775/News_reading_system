from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import mysql.connector as sql

# Create your views here.
def login(request):

    if request.method == 'POST':
        conn = sql.connect(host="localhost",user="root",passwd="v49775",database="news")
        cursor=conn.cursor()
        email = request.POST['email']
        password = request.POST['password']
        # user = User.is_authenticated(username=email,password=password)
        query = "select * from user where Email='{}' and Password='{}'".format(email, password)
        cursor.execute(query)
        t =list(cursor.fetchall())
        print(t)
        if email not in t and password not in t:
            print(email,password)
            print(t)
            email1={'email':email}
            return redirect("speak")
        # if email in t:
        #
        #     return redirect("speak")
        else:
            msg={"invalid":"Invalid Credentials"}
            return render(request,'login.html',msg)

    else:
        return render(request,"login.html")
        # query = "select * from user where Email='{}' and Password='{}'".format(email,password)
        # cursor.execute(query)
        # t =cursor.fetchall()


        # if t == ():
        #     error = {"invalid":"Your Cradintial is invalid"}
        #     return render(request,"login.html",error)
        #     # return HttpResponse("<h1>Error</h1>")
        # else:
        #     if t == (email):
        #         return render(request,"speak.html")
        #     else:
        #         return HttpResponse("<h1>Error</h1>")

    return render(request,'login.html')

