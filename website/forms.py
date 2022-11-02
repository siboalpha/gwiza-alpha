from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import ContactMessage

class ContactFrom(ModelForm):
    class Meta:
        model = ContactMessage
        fields = {'first_name','last_name', 'phone_number', 'email', 'message'}
        widgets = {
            'first_name': TextInput(attrs={'class':'form-control','placeholder': 'Your first name'}),
            'last_name': TextInput(attrs={'class':'form-control','placeholder': 'Your last name'}),
            'phone_number': TextInput(attrs={'class':'form-control','placeholder': 'Your phone number'}),
            'email': EmailInput(attrs={'class':'form-control','placeholder': 'Your email address'}),
            'message': Textarea(attrs={'class':'form-control','placeholder': 'Type your message here'}),
        }