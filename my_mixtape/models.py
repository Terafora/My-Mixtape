from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


# Genre choices for mixtapes

GENRES = [
    ('Misc.', 'Misc.'),
    ('Rock', 'Rock'),
    ('Pop', 'Pop'),
    ('J-Pop', 'J-Pop'),
    ('K-Pop', 'K-Pop'),
    ('C-Pop', 'C-Pop'),
    ('Latin', 'Latin'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Electronic', 'Electronic'),
    ('R&B', 'R&B'),
    ('Country', 'Country'),
    ('Jazz', 'Jazz'),
    ('Jazz Fusion', 'Jazz Fusion'),
    ('Classical', 'Classical'),
    ('Folk', 'Folk'),
    ('Blues', 'Blues'),
    ('Punk', 'Punk'),
    ('Metal', 'Metal'),
    ('Reggae', 'Reggae'),
    ('Soul', 'Soul'),
    ('Funk', 'Funk'),
    ('Disco', 'Disco'),
    ('Gospel', 'Gospel'),
    ('World', 'World'),
    ('Indie', 'Indie'),
    ('Ambient', 'Ambient'),
    ('Experimental', 'Experimental'),
    ('Soundtrack', 'Soundtrack'),
    ('Holiday', 'Holiday'),
    ('Comedy', 'Comedy'),
    ('Spoken Word', 'Spoken Word'),
    ('Children\'s', 'Children\'s'),
    ('Other', 'Other'),
]


# Mixtape collection and Mixtape models


class Mixtape_Collection(models.Model):
    """A collection of mixtapes the user has created"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mixtape_collections')
    name = models.CharField(max_length=200, null = False, blank = False)

    def __str__(self):
        return self.name
    
# Signal to create a Mixtape_Collection instance upon user creation
@receiver(post_save, sender=User)
def create_user_mixtape_collection(sender, instance, created, **kwargs):
    if created:
        Mixtape_Collection.objects.create(owner=instance, name=f"{instance.username}'s Mixtapes")

class Mixtape(models.Model):
    """A mixtape created by the user which will be in their collection"""
    collection = models.ForeignKey(Mixtape_Collection, on_delete=models.CASCADE, related_name='mixtapes')
    name = models.CharField(max_length=200, null = False, blank = False)
    image = ResizedImageField(size=[400, None], quality=75, upload_to='my_mixtape/', force_format='WEBP', null = True, blank = True)
    image_alt = models.CharField(max_length=100, null = True, blank = True)
    about = RichTextField(max_length= 1000 ,null = True, blank = True)
    genre = models.CharField(max_length=32, choices=GENRES, default = 'Misc.')
    posted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.collection.name}"
    
    class Meta:
        ordering = ['-posted_date']

class Track(models.Model):
    """A track in a mixtape"""
    mixtape = models.ForeignKey(Mixtape, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=200, null=False, blank=False)
    artist = models.CharField(max_length=200, null=True, blank=True)
    song_link = models.URLField(max_length=500, null=False, blank=False)
    genre = models.CharField(max_length=32, choices=GENRES, default = 'Misc.')
    posted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.mixtape.name})"
    
    class Meta:
        ordering = ['-posted_date']