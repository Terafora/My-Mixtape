from django.urls import path
from .views import Index, About, Library

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('library/', Library.as_view(), name='library'),
]
