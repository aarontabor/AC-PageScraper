from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from pageScraper.models import Event, Race


class TestMapEventView(TestCase):

  def setUp(self):
    self.workAroundForSessionBug()

  def workAroundForSessionBug(self):
    # work around for a know bug in dJango
    # in testing framework, session only works with a user context
    User.objects.create_user('bill', 'bill@email.com', 'password')
    self.client.login(username='bill', password='password')

  def setSession(self, sessionDict):
    session = self.client.session
    for k, v in sessionDict.items():
      session[k] = v
    session.save()

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

