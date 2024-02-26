from django.db import models

class BatuModell(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    # Add other fields as needed

    def __str__(self):
        return self.name
