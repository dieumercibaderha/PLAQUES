from django.db import models
from django.db.models.signals import pre_save, pre_delete, pre_migrate, pre_init

# Create your models here.

class Proprietaires(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.CharField(max_length=200)
    Mail=models.EmailField(max_length=100)
    Tel=models.CharField(max_length=15)
    Photo=models.ImageField(upload_to="photoapp", blank=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Propriètaire'
        verbose_name_plural = 'Propriètaires'
 
    def __str__(self):
        return self.nom
    
class Genre(models.Model):
    Genre=models.CharField(max_length=100)
    Description=models.TextField(max_length=600)
    
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
    def __str__(self):
        return self.Genre
        
        
class Utilisation(models.Model):
    Type_utilisation=models.CharField(max_length=100)   
    Description=models.TextField(max_length=600)
    
    class Meta:
        verbose_name = 'Utilisation'
        verbose_name_plural = 'Utilisations'
        
    def __str__(self):
        return self.Type_utilisation
    
class Pays(models.Model):
    Nom_pays=models.CharField(max_length=100) 
    
    class Meta:
        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'
    def __str__(self):
        return self.Nom_pays
   
class Moto(models.Model):
    Marque=models.CharField(max_length=50)
    Nom=models.CharField(max_length=100)
    Annee=models.DateField(auto_now=True)
    genre_moto=models.ForeignKey(Genre , on_delete=models.CASCADE)
    Couleur=models.CharField(max_length=50)
    Source_energie=models.CharField(max_length=50)
    Type_utilisation=models.ForeignKey(Utilisation, on_delete=models.CASCADE)
    Pays_fabrication=models.ForeignKey(Pays, on_delete=models.CASCADE)
    Num_chassis=models.CharField(max_length=50)
    Num_moteur=models.CharField(max_length=50)
    Date_circulation=models.DateTimeField(auto_now=False, auto_now_add=False)
    Date_identification=models.DateTimeField(auto_now=True)
    proprietaire=models.ForeignKey(Proprietaires, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Moto'
        verbose_name_plural = 'Motos'
    
    def __str__(self):
        return self.Nom

class Exoneration(models.Model):
    type_Exoneration=models.CharField(max_length=200)    
    Description=models.TextField(max_length=600)
    
    class Meta:
        verbose_name = 'Exoneration'
        verbose_name_plural = 'Exonerations'
    def __str__(self):
        return self.type_Exoneration

class Enregistrement(models.Model):
    moto=models.ForeignKey(Moto, on_delete=models.CASCADE, unique=True)
    Num_Plaque=models.CharField(max_length=50, unique=True)
    Proprietaire=models.ForeignKey(Proprietaires, on_delete=models.CASCADE, default=1)
    Photo_proprietaire=models.ImageField(upload_to="photoapp", blank=True)
    Exonerations=models.ForeignKey(Exoneration, on_delete=models.CASCADE)
    dates=models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Vente'
        verbose_name_plural = 'Ventes'
        
    def __str__(self):
        return self.Num_Plaque
    
class Controle(models.Model):
    Num_Plaque=models.CharField(max_length=100)
    Exonerations=models.ForeignKey(Exoneration, on_delete=models.CASCADE)
    Proprietaires=models.ForeignKey(Proprietaires, on_delete=models.CASCADE) 
    Dates=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Controle'
        verbose_name_plural = 'Controle'
    def __str__(self):
          return self.Num_Plaque
  
     

        
        

#pre_save.connect(copy_data, sender=Enregistrement)
#pre_delete.connect(delete_data, sender=Enregistrement)
#pre_migrate.connect(update_data, sender=Enregistrement)

