from django.http import HttpRequest
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .forms import ContactForm
from django.shortcuts import render,HttpResponse

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = "this is"
        return context
    



# contact form
class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # Process the data in form.cleaned_data
        # For example, you can send an email with the form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # Implement your processing logic here

        return HttpResponse('Thank you for your message.')
    



   





