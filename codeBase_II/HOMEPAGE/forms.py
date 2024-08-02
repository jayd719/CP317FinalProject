from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
    def print_from(self):
         print(self.name)
         print(self.message)


# ask user what kind of car they want to buy
class CarForm(forms.Form):
    CAR_CHOICES = [
        ('toyota', 'Toyota'),
        ('honda', 'Honda'),
        ('ford', 'Ford'),
        ('bmw', 'BMW'),
        ('audi', 'Audi'),
    ]
    car_choice = forms.ChoiceField(choices=CAR_CHOICES, label="Which kind of car do you buy?")