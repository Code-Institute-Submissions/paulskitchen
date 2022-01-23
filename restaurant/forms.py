from django import forms

from .models import Contact, Booking

class DateInput(forms.DateInput):
    input_type = 'date' 

class TimeInput(forms.TimeInput):
    input_type = 'time' 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 
            'email',
            'message',
        ]

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user',
            'date',
            'time',
            'guests',
        ]
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }