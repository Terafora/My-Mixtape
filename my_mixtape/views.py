from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "my_mixtape/index.html"