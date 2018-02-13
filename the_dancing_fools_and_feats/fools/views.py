from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'fools/index.html'

class ClassAndDanceView(TemplateView):
    template_name = 'fools/classes_and_dance.html'
