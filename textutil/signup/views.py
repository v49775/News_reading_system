from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
import mysql.connector as sql


# Create your views here.

def signup(request):

    if request.method == 'POST':
        conn = sql.connect(host="localhost",user="root",passwd="v49775",database="news")
        cursor=conn.cursor()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        sex = request.POST['sex']
        email = request.POST['email']
        password = request.POST['password']

        query = "insert into user values('{}','{}','{}','{}','{}')".format(first_name,last_name,sex,email,password)
        cursor.execute(query)
        conn.commit()

        print("user created")
        msg = {'msg': ' Register Successfully'}
        return render(request, 'signup.html', msg)

    else:
        return render(request,'signup.html')