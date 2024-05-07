from django import forms
from .models import Commentaire
from django.forms import TextInput,FileInput

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['nom', 'photo', 'message']
        widgets = {
            'nom': TextInput(attrs={
                'class': "form-controlinput",
                'placeholder': 'Votre nom',
                
            }),
            'message': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Votre message'
            }),
            'photo': FileInput(attrs={
                'class': "photochoice", 
            }),

        }
