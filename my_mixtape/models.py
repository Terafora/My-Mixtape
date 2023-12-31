from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField


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
    ('Bossa Nova', 'Bossa Nova'),
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


# # Mixtape collection and Mixtape models

class Mixtape(models.Model):
    """A mixtape created by the user which will be in their collection"""
    collection = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mixtapes')  # noqa
    name = models.CharField(max_length=200, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    about = RichTextField(max_length=1000, null=True, blank=True)
    genre = models.CharField(max_length=33, choices=GENRES, default='Misc.')
    posted_date = models.DateTimeField(auto_now=True)


class Post(models.Model):
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
    )

    def __str__(self):
        return f"{self.name}"


class Track(models.Model):
    """A track in a mixtape"""
    mixtape = models.ForeignKey(Mixtape, on_delete=models.CASCADE, related_name='tracks')  # noqa
    title = models.CharField(max_length=200, null=False, blank=False)
    artist = models.CharField(max_length=200, null=True, blank=True)
    song_link = models.URLField(max_length=500, null=False, blank=False)
    genre = models.CharField(max_length=32, choices=GENRES, default='Misc.')
    posted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.mixtape.name})"

    class Meta:
        ordering = ['-posted_date']
