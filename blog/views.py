from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template

from django.shortcuts import render,get_object_or_404
from blog.forms import AuthorForm,Authentic,UserProfile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from blog.models import input
from datetime import datetime
     
...
        
def main_page(request):
    qs = input.objects.all()
    qs = sorted(qs,key=lambda x:x.date,reverse=False)
    if request.method=="POST":
         mydate=request.POST.get("date",)
         qs = input.objects.filter(date=mydate)
         qs = sorted(qs,key=lambda x:x.time,reverse=False)
         return render(request,"blog/index_page.html",{"qs":qs,"mydate":mydate})

        


    else:
          return render(request,"blog/index_page.html",{"qs":qs,})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("main_page"))

@login_required
def form_name_view(request):
    forme=AuthorForm()
    if request.method=="POST":
        forme=AuthorForm(request.POST)

        if forme.is_valid():
            forme.save()
            return HttpResponse("successfully submitted !" )
            
        else:
            print("error")    
    return render(request,"blog/form_page.html",{"forme":forme })        

def authentication_view(request):
    registered = False
    
    if request.method=="POST":
     auth=Authentic(request.POST )

     if auth.is_valid():
         auth=auth.save(commit=False)
         auth.set_password(auth.password)   
         #hashing the password
         auth.save()
         registered=True


     else :
         print("error")
    else:
        auth=Authentic()     
    return render(request,"blog/signup.html",{"auth":auth,"registered":registered })        


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)


        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("blog:form_name",))
        else:
            return HttpResponse("invalid username and password")
    else :
        return render(request,"blog/login.html",{})