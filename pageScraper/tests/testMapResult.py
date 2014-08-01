from pageScraper.tests.viewTestCase import ViewTestCase
from django.core.urlresolvers import reverse
from pageScraper.models import Runner, Race, Event, Result


class TestMapResultView(ViewTestCase):

  def test_wiring(self):
    self.client.get(reverse('pageScraper:map_results'))

  def test_saves_results(self):

    runner = Runner(name='Johnny', sex='m')
    runner.save()

    race = Race(
        name='TestRace', 
        location='Here',
        raceDirector='race Dir',
        date='2014-05-04',
        )
    race.save()

    event = Event(name='5k', race=race)
    event.save()

    self.setSession({
      'results': [['1', '123', 'Tim Test', '20:12']],
      'runner_ids': [runner.id],
      'event_id': event.id,
    })

    self.client.post(reverse('pageScraper:map_results'), {
      'position': 0,
      'bib': 1,
      'gunTime': 3,
    })

    result_id = self.client.session['result_ids'][0]
    result = Result.objects.get(pk=result_id)

    self.assertEqual(1, result.position)
    self.assertEqual(runner, result.runner)
