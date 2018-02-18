from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'fools/pages/index.html'

class ClassAndDanceView(TemplateView):
    template_name = 'fools/pages/classes_and_dance.html'

class StaffView(TemplateView):
    template_name = 'fools/pages/staff.html'

class GettingHereView(TemplateView):
    template_name = 'fools/pages/getting_here.html'
