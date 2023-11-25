from django.contrib import admin
from .models import Mixtape_Collection, Mixtape, Track


# Register your models here.

@admin.register(Mixtape_Collection)
class Mixtape_CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    list_filter = ('owner',)

@admin.register(Mixtape)
class MixtapeAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection')
    list_filter = ('collection',)

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'mixtape', 'song_link')
    list_filter = ('mixtape', 'genre')