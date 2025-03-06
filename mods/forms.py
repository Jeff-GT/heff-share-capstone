from django import forms
from .models import Mod, ModImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = Mod
        fields = ['title', 'description','cover_image', 'file', 'game', 'modtags'] 
        widgets = {
            'modtags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

class RatingForm(forms.Form):
    RATING_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    mod_id = forms.IntegerField(widget=forms.HiddenInput())