from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView  # noqa
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import Track, Mixtape
from .forms import MixtapeForm

# Point to the correct general templates


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

class AddMixTape(LoginRequiredMixin, CreateView):
    """Add a mixtape to a mixtape collection"""
    model = Mixtape
    form_class = MixtapeForm  # Use your custom form class here
    template_name = "my_mixtape/add_mixtape.html"
    success_url = '/library/'

    # Additional test_func to ensure the user adding a mixtape is the creator
    def test_func(self):
        mixtape = self.get_object().mixtape
        return self.request.user == mixtape.collection

    def form_valid(self, form):
        form.instance.collection = self.request.user
        return super().form_valid(form)


class OpenTrackList(DetailView):
    """Open a list of tracks in a mixtape"""
    model = Mixtape
    template_name = "my_mixtape/track_list.html"
    context_object_name = 'mixtape'
    pk_url_kwarg = 'mixtape_id'


class DeleteMixtape(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a mixtape"""
    model = Mixtape
    success_url = '/library/'

    def test_func(self):
        mixtape = self.get_object()
        return self.request.user == mixtape.collection


class EditMixTape(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a mixtape"""
    model = Mixtape
    fields = ['name', 'image', 'image_alt', 'about', 'genre']
    template_name = "my_mixtape/edit_mixtape.html"
    success_url = '/library/'

    # Additional test_func to ensure the user editing the mixtape is the creator  # noqa
    def test_func(self):
        mixtape = self.get_object()
        return self.request.user == mixtape.collection

    def get_queryset(self):
        return Mixtape.objects.filter(collection=self.request.user)


# View for Track objects

class AddTrack(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Add a track to a mixtape"""
    model = Track
    fields = ['title', 'artist', 'genre', 'song_link']
    template_name = "my_mixtape/add_track.html"
    success_url = '/mixtape/{mixtape_id}/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixtape_id = self.kwargs.get('mixtape_id')
        context['mixtape'] = get_object_or_404(Mixtape, pk=mixtape_id)
        return context

    def form_valid(self, form):
        mixtape_id = self.kwargs.get('mixtape_id')
        mixtape = get_object_or_404(Mixtape, pk=mixtape_id)
        form.instance.mixtape = mixtape
        return super().form_valid(form)

    # Additional test_func to ensure the user adding the track is the creator
    def test_func(self):
        mixtape_id = self.kwargs.get('mixtape_id')
        mixtape = get_object_or_404(Mixtape, pk=mixtape_id)
        return self.request.user == mixtape.collection

    def get_success_url(self):
        return reverse('mixtape_detail', kwargs={'mixtape_id': self.kwargs.get('mixtape_id')})  # noqa


class UpdateTrack(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update a track"""
    model = Track
    fields = ['title', 'artist', 'genre', 'song_link']
    template_name = "my_mixtape/update_track.html"
    pk_url_kwarg = 'track_id'

    # Additional test_func to ensure the user editing the track is the creator
    def test_func(self):
        mixtape = self.get_object().mixtape
        return self.request.user == mixtape.collection

    def get_success_url(self):
        return reverse('mixtape_detail', kwargs={'mixtape_id': self.object.mixtape_id})  # noqa


class DeleteTrack(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a track"""
    model = Track

    def get_success_url(self):
        # Obtain the mixtape_id from the URL kwargs
        mixtape_id = self.kwargs['mixtape_id']
        return reverse_lazy('mixtape_detail', kwargs={'mixtape_id': mixtape_id})  # noqa

    # Additional test_func to ensure the user deleting the track is the creator
    def test_func(self):
        mixtape = self.get_object().mixtape
        return self.request.user == mixtape.collection

    def get_object(self, queryset=None):
        # Fetch the track based on both mixtape_id and track_id
        mixtape_id = self.kwargs['mixtape_id']
        track_id = self.kwargs['track_id']
        track = Track.objects.get(mixtape_id=mixtape_id, pk=track_id)
        return track

    def delete(self, request, *args, **kwargs):
        # Override the delete method to include mixtape_id in deletion criteria
        mixtape_id = self.kwargs['mixtape_id']
        track_id = self.kwargs['track_id']
        track = self.get_object()
        track.delete()
        return HttpResponseRedirect(self.get_success_url())
