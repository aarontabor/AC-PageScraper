from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from pageScraper.models import Runner


class TestMapRunnerView(TestCase):

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

