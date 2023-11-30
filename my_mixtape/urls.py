from django.urls import path
from .views import Index, About, Library, OpenTrackList, AddMixTape

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('library/', Library.as_view(), name='library'),
    path('mixtape/<int:mixtape_id>/', OpenTrackList.as_view(), name='mixtape_detail'),
    path('add_mixtape/', AddMixTape.as_view(), name='add_mixtape'),
]
