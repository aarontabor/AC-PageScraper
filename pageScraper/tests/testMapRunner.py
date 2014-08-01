from pageScraper.tests.viewTestCase import ViewTestCase
from django.core.urlresolvers import reverse
from pageScraper.models import Runner


class TestMapRunnerView(ViewTestCase):

  def test_wiring(self):
    self.client.get(reverse('pageScraper:map_runners'))

  def test_builds_runner_correctly(self):
    self.setSession({
      'headers': ['name', 'sex'],
      'results': [['Tom', 'm']],
    })

    self.client.post(reverse('pageScraper:map_runners'), {
      'name': 0,
      'sex': 1,
    })

    runner_id = self.client.session['runner_ids'][0]
    runner = Runner.objects.get(pk=runner_id)
    self.assertEquals('Tom', runner.name)
    self.assertEquals('m', runner.sex)

