import unittest

import googleapiclient
import pytest
from googleapiclient import sample_tools


def get_service():
    service, flags = sample_tools.init(
        [__file__], 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar')
    return service


class CalendarPositiveTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = get_service()

        calendar_properties = {
            'summary': 'test calendar',
            'timeZone': 'America/Los_Angeles'
        }
        cls.calendar = cls.service.calendars().insert(body=calendar_properties).execute()

        cls.event = cls.service.events().quickAdd(
            calendarId=cls.calendar['id'],
            text='Appointment at Somewhere today 10am-10:25am'
            ).execute()

    def test_event_status(self):
        assert self.event['status'] == 'confirmed'

    def test_event_summary(self):
        assert self.event['summary'] == 'Appointment at Somewhere'

    def test_event_is_listed_once(self):
        events = self.service.events().list(
            calendarId=self.calendar['id'], pageToken=None).execute()
        items = events['items']
        assert len(items) == 1
        assert items[0]['id'] == self.event['id']

    @classmethod
    def tearDownClass(cls):
        cls.service.calendars().delete(calendarId=cls.calendar['id']).execute()


class CalendarNegativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = get_service()

    def test_unknown_calendar_id_raises(self):
        with pytest.raises(googleapiclient.errors.HttpError) as exc_info:
            self.service.events().quickAdd(
                calendarId='UNKNOWN_CALENDAR_ID', text='Appointment at Somewhere today 10am-10:25am'
                ).execute()
        assert exc_info.value.resp.status == 404
