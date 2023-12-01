from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Mixtape

class NoteForm(forms.ModelForm):
    """Form to add a note"""
    title = forms.CharField(label='Title')

    class Meta:
        model = Mixtape
        fields = ['title', 'note']

        widgets = {
            "note": forms.Textarea(attrs={'rows': 2}),
        }

        labels = {
            'note': 'Note',
        }