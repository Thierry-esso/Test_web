from django.db import models

# Create your models here.
class Capsules(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    libelle = models.CharField(max_length=50)
    forme = models.CharField(max_length=50)
    couleur = models.CharField(max_length=50)
    description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)