from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Username'}), required=True)
    email = forms.EmailField(
        widget=forms.EmailInput(
          attrs={
            'placeholder':'example@email.com', 'type':'email'
          }
        ), 
      required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)