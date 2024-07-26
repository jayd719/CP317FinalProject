from django.shortcuts import render

def homepage(request):
    return render(request,"base.html")



def searchForDoctor(request):
    data =''
    return render("components/searchBoxResultItem.html",data= data)