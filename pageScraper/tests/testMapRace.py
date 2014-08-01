from pageScraper.tests.viewTestCase import ViewTestCase
from django.core.urlresolvers import reverse
from pageScraper.models import Race


class TestMapRaceView(ViewTestCase):

  def test_wiring(self):
    self.client.get(reverse('pageScraper:map_race'))

  def test_set_initial_values(self):
    session = self.client.session
    session['name'] = 'Terry Test'
    session.save()

    response = self.client.get(reverse('pageScraper:map_race'))
    
    self.assertContains(response, 'Terry Test')

  def test_puts_race_in_session(self):
    self.client.post(reverse('pageScraper:map_race'), {
      'name': 'Tester Ten K',
      'location': 'Testland',
      'raceDirector': 'Terry Test',
      'date': '2014-10-05',
    }, follow = True)
    session = self.client.session
    self.assertIsInstance(session.get('race_id'), int)
