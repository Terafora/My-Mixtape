from django import forms
from .models import Mixtape


class MixtapeForm(forms.ModelForm):
    class Meta:
        model = Mixtape
        fields = ['name', 'image', 'image_alt', 'about', 'genre']
