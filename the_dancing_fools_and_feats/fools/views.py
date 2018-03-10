from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from django.conf import settings

from .models import WeeklyEvent, MonthlyEvent, YearlyEvent


class GoogleMapContext(ContextMixin):
    GOOGLE_API_BASE = 'https://maps.googleapis.com/maps/api/'
    GOOGLE_MAP_ADDRESS = 'The+Cambridge+Masonic+Hall,Cambridge,MA'
    MAP_API_KEY = f'&key={settings.GOOGLE_API_KEY}'
    FOOLS_MARKER = f'&markers=color:red%7C{GOOGLE_MAP_ADDRESS}'
    MAP_STYLES = f'&style=feature:poi%7Cvisibility:off'
    PORTER_SQUARE_VISIBLE = f'&visible=Porter+Square+Station,Cambridge,MA'
    PARKING_MAP_COORDS = [
        '42.392390,-71.122414',
        '42.391968,-71.122235',
        '42.391825,-71.122079',
        '42.391532,-71.122463',
        '42.391887,-71.123160',
        '42.392390,-71.122414'
    ]
    PARKING_MAP_OVERLAY = (f'&path=color:0x0A0A0AFF'
                           f'|weight:1'
                           f'|fillcolor:0x00FF00AA'
                           f'|{"|".join(PARKING_MAP_COORDS)}')
    MAP_PARAMS_BASE = f'{MAP_API_KEY}{FOOLS_MARKER}{MAP_STYLES}'
    STREET_VIEW_PARAMS = (f'&location=42.389711,-71.1204118'
                          f'&fov=65&heading=200'
                          f'&pitch=18'
                          f'{MAP_API_KEY}')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'GOOGLE_API_KEY': self.MAP_API_KEY,
            'GOOGLE_MAP_ADDRESS': self.GOOGLE_MAP_ADDRESS,
            'PARKING_MAP_PARAMS':
                f'{self.MAP_PARAMS_BASE}{self.PARKING_MAP_OVERLAY}',
            'LOCATION_MAP_PARAMS':
                f'{self.MAP_PARAMS_BASE}{self.PORTER_SQUARE_VISIBLE}',
            'STREET_VIEW_PARAMS': self.STREET_VIEW_PARAMS,
            'G_MAPS_API': self.GOOGLE_API_BASE
        })
        return context


class IndexView(TemplateView, GoogleMapContext):
    template_name = 'fools/pages/index.html'


class ClassAndDanceView(TemplateView):
    template_name = 'fools/pages/classes_and_dance.html'


class StaffView(TemplateView):
    template_name = 'fools/pages/staff.html'


class GettingHereView(TemplateView, GoogleMapContext):
    template_name = 'fools/pages/getting_here.html'


class ContactView(TemplateView):
    template_name = 'fools/pages/contact.html'


class WCSInBostonView(TemplateView):
    template_name = 'fools/pages/wcs_in_boston.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # retrieve all dance events
        weekly_events = WeeklyEvent.objects.all()
        monthly_events = MonthlyEvent.objects.all()
        # combine monthly and weekly events into a combined list
        regular_events = [*list(weekly_events), *list(monthly_events)]
        regular_events.sort(key=lambda evt: evt.order)

        yearly_events = YearlyEvent.objects.all()

        context.update({
            'regular_events': regular_events,
            'yearly_events': yearly_events,
        })

        return context
