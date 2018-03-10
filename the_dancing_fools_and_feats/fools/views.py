import re
import logging

from bs4 import BeautifulSoup
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from django.conf import settings
import requests

from .models import WeeklyEvent, MonthlyEvent, YearlyEvent

logger = logging.getLogger(__name__)


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

    def get_context_data(self, **kwargs):
        """
        In order to display the most recent instagram post from The Dancing
        Fools, a brittle hack needs to be implemented to get around significant
        restrictions of the Instagram API. It does not allow deterministic
        retrieval of recent post IDs without significant authentication
        overhead.

        This method sends a request to The Dancing Fools' Instagram page,
        and parses the returned JSX for the first instance of an attribute
        associated with post ids, `shortcode`. The ID is then read from

        Due to the high probability of this breaking at any time, it will
        fail silently very easily. In this case, the instagram post will not
        display on the main page.
        """
        context = super().get_context_data(**kwargs)

        # TODO: Make error handling more robust, log and alert on failures
        try:
            body = requests.get('https://www.instagram.com/thedancingfools/')
            soup = BeautifulSoup(body.text, 'html.parser')
            # find first occurrence of an instagram post ID, then parse
            # the id's value
            match = re.search(r'"shortcode":"\w+"', soup.text)
            if not match.group():
                return context
            post_id = match.group().split(':')[1].strip('"')
            resp = requests.get(f'https://api.instagram.com/oembed'
                                f'?url=http://instagr.am/p/{post_id}/')
            json_resp = resp.json()

            if json_resp.get('html', None):
                context['instagram_embed'] = json_resp['html']
        except Exception as err:
            logger.error('Failed to retrieve instagram post for index!')
            logger.exception(err)

        return context


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
