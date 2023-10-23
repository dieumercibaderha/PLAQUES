from typing import Any
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Userform(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
class Motoforms(forms.ModelForm):
    Marque=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez la Marque'
        }
    ))
    Nom=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez le nom'
        }
    ))
    Couleur=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez la couleur '
        }
    ))
    Source_energie=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez la Source_energie'
        }
    ))
    Num_chassis=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez le num_chassis'
        }
    ))
    Num_moteur=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez le num_moteur'
        }
    ))
    class Meta:
        model=Moto
        fields=('Marque','Nom', 'genre_moto', 'Couleur', 'Source_energie', 'Type_utilisation', 'Pays_fabrication', 'Num_chassis', 'Num_moteur', 'Date_circulation', 'proprietaire')
        
class Proforms(forms.ModelForm):
    nom=forms.CharField(label='', help_text="Nom_pro", widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez le nom'
        }
    ))
    adresse=forms.CharField(label='', initial='Nom ', widget=forms.TextInput(
        attrs={
            'placeholder':"Entrez l'addresse",
            'li':'',
        }
    ))
    Mail=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez Votre Mail',
            'li':''
        }
    ))
    Tel=forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrez numero Tel',
            'li':''
        }
    ))
    class Meta:
        model=Proprietaires
        fields=('nom', 'adresse', 'Mail', 'Tel', 'Photo')
        
class Exoforms(forms.ModelForm):
    class Meta:
        model=Exoneration
        fields='__all__'

class Genreforms(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'      
class Utiliforms(forms.ModelForm):
    class Meta:
        model=Utilisation
        fields='__all__'   
        
class Paysforms(forms.ModelForm):
    class Meta:
        model=Pays
        fields='__all__'