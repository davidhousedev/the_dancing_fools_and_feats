from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'fools/pages/index.html'

class ClassAndDanceView(TemplateView):
    template_name = 'fools/pages/classes_and_dance.html'
