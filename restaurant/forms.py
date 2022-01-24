from django import forms

from .models import Contact, Booking

class DateInput(forms.DateInput):
    input_type = 'date' 

class TimeInput(forms.TimeInput):
    input_type = 'time' 

class NumberInput(forms.NumberInput):
    input_type = 'number'

class TextInput(forms.TextInput):
    input_type = 'text'
    
class EmailInput(forms.EmailInput):
    input_type = 'email'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 
            'email',
            'message',
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'message': TextInput(attrs={'class': 'form-control'}),
        }

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
            'date': DateInput(attrs={'class': 'form-control'}),
            'time': TimeInput(attrs={'class': 'form-control'}),
            'guests': NumberInput(attrs={'class': 'form-control'}),
        }

#home page contact form
class HomeContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 
            'email',
            'message',
        ]