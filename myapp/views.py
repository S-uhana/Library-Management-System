from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .models import *

from myapp.models import Book

# Create your views here.


def Home(request):
    return render(request,"home.html")

def Index(request):
    return render(request,"index.html")

def Insert(request):
    return render(request,"insert.html")

def InsertData(request):
    bname = request.POST['bname']
    auth = request.POST['auth']
    price = request.POST['price']
    
    newuser = Book.objects.create(bname=bname,auth=auth,price=price)
    return redirect('showpage')

def ShowPage(request):
    all_data = Book.objects.all()
    return render(request,"show.html",{'key1':all_data})

def Edit(request):
    return render(request,"Edit.html")

def EditPage(request,pk):
    get_data = Book.objects.get(id=pk)
    return render(request,"Edit.html",{'key2':get_data})



def UpdateData(request,pk):
    udata = Book.objects.get(id=pk)
    udata.Name = request.POST['bname']
    udata.auth = request.POST['auth']
    udata.price = request.POST['price']
    udata.save()
    return redirect('showpage')

def Deletedata(request,pk):
    deleted = Book.objects.get(id=pk)
    deleted.delete()
    return redirect('showpage')

def AdminHome(request):
    return render(request,"AdminHome.html")

def RegisterUser(request):
    if request.method == "POST":
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
  
        user = UserMaster.objects.filter(email=email) 
        if user:
            message = "user already exists" 
            return render(request,"signup.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = UserMaster.objects.create(role=role,email=email,password=password)
                return render(request,"Login.html")
            else:
                return redirect('signup')
    else:
        return render(request,"signup.html")      
  
    
  



def LoginUser(request): 
    if request.method == "POST":
        email =request.POST['email']
        password = request.POST['password']
        
        user = UserMaster.objects.get(email=email,password=password) 
        
        if user is None:
            message = "Incorrect password"
            return render(request,"Login.html",{'msg2':message})
        else: 
            if user.role == "Student":    
               return redirect('index')  
            else:
                return redirect('admin') 
            
    else:
        return render(request,"Login.html")
        

def StudShow(request):
    data = Book.objects.all()
    return render(request,"StudShow.html",{'key3':data})
    