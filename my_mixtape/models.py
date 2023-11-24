from django.db import models
from django.contrib.auth.models import User



# Mixtape collection and Mixtape models


class Mixtape_Collection(models.Model):
    """A collection of mixtapes the user has created"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mixtape_collections')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Mixtape(models.Model):
    """A mixtape created by the user which will be in their collection"""
    collection = models.ForeignKey(Mixtape_Collection, on_delete=models.CASCADE, related_name='mixtapes')
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.collection.name}"
