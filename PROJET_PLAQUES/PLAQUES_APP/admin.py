from django.contrib import admin
from .models import *

class Adminmoto(admin.ModelAdmin):
    list_display=('Marque','Nom', 'genre_moto', 'Couleur', 'Source_energie','Type_utilisation', 'Pays_fabrication', 'Num_chassis', 'Num_moteur', 'Date_circulation', 'proprietaire')

class AdminGenre(admin.ModelAdmin):
    list_display=('id', 'Genre', 'Description')
class AdminPays(admin.ModelAdmin):
    list_display=('id', 'Nom_pays')  
class AdminExo(admin.ModelAdmin):
    list_display=('id', 'type_Exoneration', 'Description') 
class AdminUtili(admin.ModelAdmin):
    list_display=('id', 'Type_utilisation', 'Description')
class Adminvente(admin.ModelAdmin):
    list_display=('id', 'moto', 'Num_Plaque','Exonerations', 'dates')   
class Adminpro(admin.ModelAdmin):
    list_display=('id', 'nom', 'adresse', 'Mail', 'Photo', 'Tel')   

# Register your models here.
admin.site.register(Moto, Adminmoto)
admin.site.register(Genre, AdminGenre)
admin.site.register(Proprietaires, Adminpro)
admin.site.register(Pays, AdminPays)
admin.site.register(Exoneration, AdminExo)
admin.site.register(Utilisation, AdminUtili)
admin.site.register(Enregistrement, Adminvente)