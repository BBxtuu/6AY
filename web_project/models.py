# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()  # Hier wird das 'age'-Feld hinzugefügt

    def __str__(self):
        return self.name
