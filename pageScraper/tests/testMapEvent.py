from pageScraper.tests.viewTestCase import ViewTestCase
from django.core.urlresolvers import reverse
from pageScraper.models import Event, Race


class TestMapEventView(ViewTestCase):

  def test_wiring(self):
    self.client.get(reverse('pageScraper:map_event'))

  def test_set_initial_values(self):
    self.setSession({'eventName': '5k'})
    response = self.client.get(reverse('pageScraper:map_event'))
    self.assertContains(response, '5k')

  def test_associates_race_from_session(self):
    raceAttributes = {
        'name': 'Testy Ten K',
        'location': 'Here or There',
        'raceDirector': 'Timmy Test',
        'date': '2014-01-01',
      }
    race = Race(**raceAttributes)
    race.save()
    self.setSession({'race_id': race.id})

    response = self.client.post(reverse('pageScraper:map_event'), {
      'name': '5k',
    })

    session = self.client.session
    event = Event.objects.get(pk=session['event_id'])
    self.assertEquals(race.id, event.race.id)

