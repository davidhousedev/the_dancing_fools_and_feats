import datetime

import pytest

from ..models import DanceEvent, WeeklyEvent, MonthlyEvent, YearlyEvent

EVENT_KWARGS = {
    'title': 'Generic Event',
    'occurrence': datetime.datetime.utcnow(),
    'website_url': 'https://foo.bar.baz',
    'location': 'Location, ZZ',
    'description': 'Generic description of this event',
}


@pytest.fixture
def event(db):
    evt = DanceEvent(**EVENT_KWARGS)
    evt.save()
    return evt


@pytest.fixture
def weekly_event(db):
    evt = WeeklyEvent(**EVENT_KWARGS)
    evt.save()
    return evt


@pytest.fixture
def monthly_event(db):
    evt = MonthlyEvent(**EVENT_KWARGS)
    evt.save()
    return evt


@pytest.fixture
def yearly_event(db):
    evt = YearlyEvent(**EVENT_KWARGS)
    evt.save()
    return evt
