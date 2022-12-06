from django.shortcuts import render,redirect
from .forms import registerForm,loginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


def register(request):


        
        form = registerForm(request.POST or None)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newuser = User(username= username)
            newuser.set_password(password)
            newuser.save()
            login(request,newuser)
            messages.info(request,"Kayıt ve giriş işlemi başarılı!")
            return redirect("index")
        
        context = {
            
            "form" : form
            
             }
        return render(request,"register.html",context)

def loginu(request):
    
    form = loginForm(request.POST or None)
    context = {
        
        "form" : form
        
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username , password = password)
        
        if user is None:
            messages.info(request,"Kullanıcı adı veya şifre hatalı!")
            return render(request,"login.html",context)
        
        messages.success(request,"Giriş işlemi başarılı!")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)


def logoutu(request):
    logout(request)
    messages.success(request,"Çıkış işlemi başarılı!")
    return redirect("index")



# Create your views here.
