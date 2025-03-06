from django import forms
from .models import Support

class ContactForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@email.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(),
        }