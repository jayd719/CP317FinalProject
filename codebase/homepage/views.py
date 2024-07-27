from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from Authentication.models import Doctor
from django.db.models import Q
from .apps import get_formatted_results
from django.core import serializers
from django.http import JsonResponse
from json import loads

def index(request):
    my_dictionary = {"a": 1, "b": 2}
    return JsonResponse(my_dictionary)

def index2(request):
    my_array = [("a", 1), ("b", 2)]
    return JsonResponse(my_array, safe=False)


    
 
def homepage(request):
    return render(request,"Homepage/homepage.html")

def redirect_to_homepage(request):
    return redirect('homepage')

def searchForDoctor(request,poll):
    query = poll
    results = []
    if query:
        results = Doctor.objects.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(speciality__icontains=query) |
            Q(languages__icontains=query) 
        )
    json_data = {
        'data':get_formatted_results(results)
    }
    return JsonResponse(json_data, safe=False)
