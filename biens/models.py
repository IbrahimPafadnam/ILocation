from django.db import models
from django.db import models
from datetime import datetime
from agents.models import Agent



class Categories(models.Model):
  nom = models.CharField(max_length=200) 
  def __str__(self):
    return self.nom


CHOIX_TYPE = ( 
    ("J","Jours"), 
    ("S","Semaines"), 
    ("M","Mois"), 
    ("V","Vente")
)

class Bien(models.Model):
  agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
  categorie = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
  type_location = models.CharField(max_length = 20, choices = CHOIX_TYPE,default = 'Mois') 
  nom = models.CharField(max_length=200)
  ville = models.CharField(max_length=100)
  quartier = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  prix = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  est_disponible = models.BooleanField(default=True)
  ajout_date = models.DateTimeField(default=datetime.now, blank=True)
 
  def __str__(self):
    return self.nom