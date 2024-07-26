from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegisteredUser, Patient, Doctor
from .models import Gender

class PatientCreationForm(UserCreationForm):
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=Gender.choices, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    street_address = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    province = forms.CharField(max_length=100, required=True)
    pincode = forms.CharField(max_length=10, required=True)

    class Meta(UserCreationForm.Meta):
        model = RegisteredUser
        fields = ('first_name', 'last_name', 'email', 'dob', 'gender', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Patient.objects.create(user=user)
        return user

class DoctorCreationForm(UserCreationForm):
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=Gender.choices, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    speciality = forms.CharField(max_length=255, required=True)
    languages = forms.CharField(max_length=255, required=True)
    street_address = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    province = forms.CharField(max_length=100, required=True)
    pincode = forms.CharField(max_length=10, required=True)

    class Meta(UserCreationForm.Meta):
        model = RegisteredUser
        fields = ('first_name', 'last_name', 'email', 'dob', 'gender', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Doctor.objects.create(user=user, speciality=self.cleaned_data['speciality'], languages=self.cleaned_data['languages'])
        return user
