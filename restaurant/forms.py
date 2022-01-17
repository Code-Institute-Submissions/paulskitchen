from django import forms

from .models import Contact, Booking

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