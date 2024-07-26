from django.shortcuts import render
from django.shortcuts import redirect

def homepage(request):
    return render(request,"Homepage/homepage.html")

def redirect_to_homepage(request):
    return redirect('homepage')

def searchForDoctor(request):
    data =''
    return render("components/searchBoxResultItem.html",data= data)