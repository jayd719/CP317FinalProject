from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import PatientCreationForm, DoctorCreationForm



def register_patient(request):
    if request.method == 'POST':
        form = PatientCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username=form.cleaned_data.get('first_name')
            messages.success(request,f'Account Created For {username}!')
            return redirect('homepage')  # Redirect to the home page or a success page
    else:
        form = PatientCreationForm()
    return render(request, 'Authentication/registerNewPatient.html', {'form': form})



def register_doctor(request):
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username=form.cleaned_data.get('first_name')
            messages.success(request,f'Account Created For {username}!')
            return redirect('homepage')  # Redirect to the home page or a success page
    else:
        form = DoctorCreationForm()
    return render(request, 'Authentication/registerNewDoctor.html', {'form': form})
