from django.db import models
from django.urls import reverse_lazy
from django import forms


class Support(models.Model):
    #username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True)
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@email.com'}), required=True)
    #subject = forms.CharField(max_length=252, widget=forms.TextInput(attrs={'placeholder':'Subject'}), required=True)
    #message = forms.CharField(widget=forms.Textarea, required=True)
    username = models.CharField(max_length=150, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    subject = models.CharField(max_length=252,blank=False, null=True)
    message = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse_lazy('support')