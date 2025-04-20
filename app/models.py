from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie=models.CharField(max_length=100)
    def __str__(self):
        return self.title

