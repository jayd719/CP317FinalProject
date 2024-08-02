
from django.urls import path
from .views import *

urlpatterns = [
    path('',ContactFormView.as_view(form_class = ContactForm,template_name = "home.html")),
    path('',HomePageView.as_view())
]


