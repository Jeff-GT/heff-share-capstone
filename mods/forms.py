from django import forms
from .models import UploadView

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadView
        fields = ['title', 'description','image', 'file'] 