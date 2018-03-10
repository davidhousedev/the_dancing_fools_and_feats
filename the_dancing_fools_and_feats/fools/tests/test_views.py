from http import HTTPStatus

from django.test import Client
import pytest

from ..models import YearlyEvent, MonthlyEvent, WeeklyEvent


class TestViews:

    @pytest.mark.django_db
    def test_event_view_context(self,
                        client: Client,
                        weekly_event: WeeklyEvent,
                        monthly_event: MonthlyEvent,
                        yearly_event: YearlyEvent):
        resp = client.get('/fools/wcs_in_boton')
        assert resp.status_code == HTTPStatus.OK
        assert yearly_event in resp.context['yearly_events']
        assert monthly_event in resp.context['regular_events']
        assert weekly_event in resp.context['regular_events']

    @pytest.mark.parametrize('url', ['/fools/getting_here', '/fools/'])
    def test_google_map_context(self, client: Client, url: str):
        resp = client.get(url)
        assert resp.status_code == HTTPStatus.OK
        assert 'GOOGLE_API_KEY' in resp.context
        assert 'G_MAPS_API' in resp.context
