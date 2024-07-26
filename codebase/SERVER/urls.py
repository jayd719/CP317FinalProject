from django.contrib import admin
from django.urls import path
from homepage.views import *
from Authentication.views import*
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',redirect_to_homepage),
    
    path('homepage',homepage,name="homepage"),
    
    path('register/patient/', register_patient, name='register_patient'),
    
    path('register/doctor/', register_doctor, name='register_doctor'),
    
    path('sign-in/',LoginView.as_view(template_name="Authentication/signIn.html",redirect_authenticated_user=True),name='signInP'),
    
    path('logout/',LogoutView.as_view(template_name="Authentication/logout.html"),name='logout'),
    
    path('search-for-a-doctor',searchForDoctor,name='search-doctor')
]
