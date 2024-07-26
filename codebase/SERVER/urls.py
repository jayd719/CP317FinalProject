from django.contrib import admin
from django.urls import path
from homepage.views import *
from Authentication.views import*



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',redirect_to_homepage),
    
    path('homepage',homepage,name="homepage"),
    
    path('register/patient/', register_patient, name='register_patient'),
    
    path('register/doctor/', register_doctor, name='register_doctor'),
]
