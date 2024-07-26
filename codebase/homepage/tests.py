import random
from datetime import date
from Authentication.models import User, Doctor, Gender

# Sample data
first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Daniel", "Laura", "James", "Olivia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
specialities = ["Cardiology", "Neurology", "Oncology", "Pediatrics", "Orthopedics", "Dermatology", "Gynecology", "Psychiatry", "Radiology", "Urology"]
languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Russian", "Portuguese", "Italian", "Hindi"]
genders = [Gender.MALE, Gender.FEMALE]

# Create 50 sample doctors
for _ in range(50):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    dob = date(random.randint(1970, 2000), random.randint(1, 12), random.randint(1, 28))
    gender = random.choice(genders)
    phone_number = f"+1-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    
    # Create user
    user = User.objects.create(
        email=email,
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        gender=gender,
        phone_number=phone_number,
    )
    user.set_password("password123")  # Set a default password
    user.save()

    # Create doctor
    speciality = random.choice(specialities)
    language = random.choice(languages)
    Doctor.objects.create(
        user=user,
        speciality=speciality,
        languages=language
    )
