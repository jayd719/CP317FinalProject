from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from Authentication.models import Doctor
from django.db.models import Q
from .apps import get_formatted_results

def homepage(request):
    return render(request,"Homepage/homepage.html")

def redirect_to_homepage(request):
    return redirect('homepage')

def searchForDoctor(request):
    query = request.GET.get('keyword')
    results = []
    if query:
        results = Doctor.objects.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(speciality__icontains=query) |
            Q(languages__icontains=query) 
        )
    return HttpResponse(get_formatted_results(results))