from django import forms
from .models import *
import datetime

class Venteform(forms.ModelForm):
    Num_Plaque=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez la num de la Plaque'
        }
    ))
    class Meta:
        model = Enregistrement
        fields=('moto', 'Num_Plaque','Exonerations')