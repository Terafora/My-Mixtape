from django.views.generic import TemplateView
from django.db import models

class Index(TemplateView):
    template_name = "my_mixtape/index.html"

class About(TemplateView):
    template_name = "my_mixtape/about.html"