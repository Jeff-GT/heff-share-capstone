from django import forms
from .models import Support

class ContactForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['username', 'email', 'subject', 'message']
        # fields = '__all__'