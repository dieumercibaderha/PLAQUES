from django import forms
from PLAQUES_APP.models import *

class Propforms(forms.ModelForm):
    class Meta:
        model=Enregistrement
        fields='__all__'