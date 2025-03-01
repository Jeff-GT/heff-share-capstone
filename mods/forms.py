from django import forms
from .models import Mod, ModImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = Mod
        fields = ['title', 'description','cover_image', 'file', 'game', 'modtags'] 
        widgets = {
            'modtags': forms.CheckboxSelectMultiple()
        }


class RatingForm(forms.Form):
    RATING_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    mod_id = forms.IntegerField(widget=forms.HiddenInput())