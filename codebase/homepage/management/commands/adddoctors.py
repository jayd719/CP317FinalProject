import random
from datetime import date
from django.core.management.base import BaseCommand
from Authentication.models import RegisteredUser, Doctor, Gender

class Command(BaseCommand):
    help = 'Add sample doctors to the database'

    def handle(self, *args, **kwargs):
        first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Daniel", "Laura", "James", "Olivia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        specialities = ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Orthopedics", "Dermatology", "Gynecology", "Psychiatry", "Radiology", "Urology"]
        languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Russian", "Portuguese", "Italian", "Hindi"]
        genders = [Gender.MALE, Gender.FEMALE]

        for _ in range(50):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            email = f"{first_name.lower()}.{last_name.lower()}.{random.randint(1, 2000)}@example.com"
            dob = date(random.randint(1970, 2000), random.randint(1, 12), random.randint(1, 28))
            gender = random.choice(genders)
            phone_number = f"+1-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
            
            user =RegisteredUser.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                gender=gender,
                phone_number=phone_number,
            )
            user.set_password("password123")
            user.save()

            speciality = random.choice(specialities)
            language = random.choice(languages)
            Doctor.objects.create(
                user=user,
                speciality=speciality,
                languages=language
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 50 doctors'))
