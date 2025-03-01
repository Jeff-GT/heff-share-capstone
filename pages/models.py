from django.db import models
from django.urls import reverse_lazy
from django import forms


class Support(models.Model):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Username'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@email.com'}), required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('support')