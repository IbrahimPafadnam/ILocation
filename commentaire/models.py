from django.db import models

class Commentaire(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom