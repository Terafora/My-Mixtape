from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.db import models
from .models import Track, Mixtape

# Point to the correct template

class Index(TemplateView):
    template_name = "my_mixtape/index.html"

class About(TemplateView):
    template_name = "my_mixtape/about.html"

class Library(TemplateView):
    template_name = "my_mixtape/library.html"

# Used for CRUD

class AddMixTape(CreateView):
    """Add a mixtape to a mixtape collection"""
    model = Mixtape
    fields = ['name', 'image', 'image_alt', 'about', 'genre']
    template_name = "my_mixtape/add_mixtape.html"
    success_url = '/library/'

    def form_valid(self, form):
        form.instance.collection = self.request.user
        return super().form_valid(form)

class AddTrack(CreateView):
    """Add a track to a mixtape"""
    model = Track
    fields = ['title', 'artist', 'genre', 'song_link']
    template_name = "my_mixtape/add_track.html"
    success_url = '/library/'

    def form_valid(self, form):
        form.instance.mixtape = Mixtape.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)