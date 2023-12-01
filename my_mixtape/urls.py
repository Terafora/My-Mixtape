from django.urls import path
from .views import Index, About, Library, OpenTrackList, AddMixTape, AddTrack, DeleteMixtape

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('library/', Library.as_view(), name='library'),
    path('add_mixtape/', AddMixTape.as_view(), name='add_mixtape'),
    path('mixtape/<int:mixtape_id>/', OpenTrackList.as_view(), name='mixtape_detail'),
    path('mixtape/delete/<int:mixtape_id>/', DeleteMixtape.as_view(), name='delete_mixtape'),
    path('<int:mixtape_id>/add_track/', AddTrack.as_view(), name='add_track'),
]
