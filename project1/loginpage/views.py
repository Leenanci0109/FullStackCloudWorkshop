from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import mysql.connector



from loginpage.models import login
# Create your views here.
def loginpage(request):
    #print("kdadk")

    if(request.GET.get('mybtn')):
        username = request.GET['username']
        password = request.GET['password']
        print("kdadk")
    #     mydb = mysql.connector.connect(
    #     host="127.0.0.1",
    #     user="root",
    #     password="root",
    #     database="login"
    #     )
        us = login.objects.all()
    #     mycursor = mydb.cursor()

    #     mycursor.execute("SELECT * FROM login_1")

    #     myresult = mycursor.fetchall()
        f=0
        for x in us:
            if((x[1]==username)and(x[2]==password)):
                f=1
        if(f==1):
            return render(request, 'loginsuccess.html', {})
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})

    



    

def loginauth():
    
    return render(request,'loginsuccess.html')