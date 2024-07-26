from django.contrib.auth.models import User
from django.db import models

# Enumeration for Gender
class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'

# Address Model
class Address(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

# Registered User Model
class RegisteredUser(User):
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    phone_number = models.CharField(max_length=15)
    User._meta.get_field('email')._unique = True
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def update_email(self, email):
        self.email = email
        self.save()

    def get_user_details(self):
        return f"{self.first_name} {self.last_name}, Email: {self.email}, Phone: {self.phone_number}"

    def get_email(self):
        return self.email

    def get_age(self):
        from datetime import date
        return date.today().year - self.dob.year

    def create_account(self):
        self.save()

    def login(self):
        pass  

    def logout(self):
        pass  


# Patient Model
class Patient(models.Model):
    user = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)
    patient_id = models.AutoField(primary_key=True)

    def create_medical_record(self, record_type):
        record = MedicalRecord(patient=self, type_of_medical_record=record_type)
        record.save()
        return record

    def update_medical_record(self, record_id, updated_data):
        record = MedicalRecord.objects.get(pk=record_id)
        for key, value in updated_data.items():
            setattr(record, key, value)
        record.save()
        return record

    def view_medical_record(self, record_id):
        return MedicalRecord.objects.get(pk=record_id)

# Doctor Model
class Doctor(models.Model):
    user = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)
    doctor_id = models.AutoField(primary_key=True)
    speciality = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)

    def write_note_on_record(self, record_id, note_text):
        record = MedicalRecord.objects.get(pk=record_id)
        note = NoteOnMedicalRecord(record=record, note_text=note_text)
        note.save()
        return note

    def view_medical_records(self, patient_id):
        return MedicalRecord.objects.filter(patient__patient_id=patient_id)

    def update_medical_record(self, record_id, updated_data):
        record = MedicalRecord.objects.get(pk=record_id)
        for key, value in updated_data.items():
            setattr(record, key, value)
        record.save()
        return record

# Medical Record Type Enumeration
class MedicalRecordType(models.TextChoices):
    ALLERGIES = 'Allergies'
    CLINICAL_VITALS = 'Clinical Vitals'
    CONDITIONS = 'Conditions'
    IMMUNIZATIONS = 'Immunizations'
    LAB_RESULTS = 'Lab Results'
    MEDICATION_RECORDS = 'Medication Records'
    PROCEDURES = 'Procedures'
    PRESCRIPTIONS = 'Prescriptions'
    VACCINATION = 'Vaccination'

# Medical Record Model
class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctors_shared_with = models.ManyToManyField(Doctor, related_name='shared_records')
    type_of_medical_record = models.CharField(max_length=50, choices=MedicalRecordType.choices)
    record_date = models.DateTimeField(auto_now_add=True)

    def get_details(self):
        return f"Record Type: {self.type_of_medical_record}, Date: {self.record_date}"

# Note On Medical Record Model
class NoteOnMedicalRecord(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='notes')
    note_date = models.DateTimeField(auto_now_add=True)
    note_text = models.TextField()

    def update_note(self, note_text):
        self.note_text = note_text
        self.save()

    def delete_note(self):
        self.delete()
