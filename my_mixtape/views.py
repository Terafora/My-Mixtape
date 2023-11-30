from django.views.generic import TemplateView, ListView, CreateView
from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Track, Mixtape

# Point to the correct template

class Index(TemplateView):
    """The home page for My Mixtape"""
    template_name = "my_mixtape/index.html"

class About(TemplateView):
    """The about page for My Mixtape"""
    template_name = "my_mixtape/about.html"

class Library(ListView):
    """The library of mixtapes for a user"""
    template_name = "my_mixtape/library.html"
    model = Mixtape
    context_object_name = 'user_mixtapes'

    def get_queryset(self):
        return Mixtape.objects.filter(collection=self.request.user)

# Used for CRUD

# Views for mixtape objects

class AddMixTape(CreateView):
    """Add a mixtape to a mixtape collection"""
    model = Mixtape
    fields = ['name', 'image', 'image_alt', 'about', 'genre']
    template_name = "my_mixtape/add_mixtape.html"
    success_url = '/library/'

    def form_valid(self, form):
        form.instance.collection = self.request.user
        return super().form_valid(form)

class OpenTrackList(ListView):
    """Open a list of tracks in a mixtape"""
    model = Mixtape
    template_name = "my_mixtape/track_list.html"
    context_object_name = 'mixtape'
    pk_url_kwarg = 'mixtape_id'
    
    #def get_queryset(self):
    #    mixtape_id = self.kwargs.get('mixtape_id')
    #    return Track.objects.filter(mixtape=mixtape_id)



# Views for track objects


class AddTrack(CreateView):
    """Add a track to a mixtape"""
    model = Track
    fields = ['title', 'artist', 'genre', 'song_link']
    template_name = "my_mixtape/add_track.html"
    #success_url = '/mixtape/{mixtape_id}/'

# This is for ensuring that I get the correct mixtape when adding a track

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixtape_id = self.kwargs.get('mixtape_id')
        context['mixtape'] = get_object_or_404(Mixtape, pk=mixtape_id)
        return context

# Access mixtape from context

    def form_valid(self, form):
        mixtape_id = self.kwargs.get('mixtape_id')
        mixtape = get_object_or_404(Mixtape, pk=mixtape_id)
        form.instance.mixtape = mixtape
        return super().form_valid(form)

    def get_success_url(self):
        mixtape_id = self.kwargs.get('mixtape_id')
        return reverse('mixtape_detail', kwargs={'mixtape_id': mixtape_id})