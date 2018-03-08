import pytest

@pytest.mark.django_db
class TestEventModels:

    def test_event_attributes(self, event):
        assert event.title
        assert event.occurrence
        assert event.website_url
        assert event.location
        assert event.description

    def test_event_time_intervals(self,
                                  weekly_event,
                                  monthly_event,
                                  yearly_event):
        assert weekly_event.frequency < monthly_event.frequency
        assert monthly_event.frequency < yearly_event.frequency
