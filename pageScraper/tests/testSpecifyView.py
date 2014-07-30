from django.test import TestCase
from django.core.urlresolvers import reverse

class TestSpecifyView(TestCase):
  def test_wiring(self):
    self.client.get(reverse('pageScraper:specify'))

  def test_it_puts_attributes_in_session(self):
    # how can I do this without actually downloading a result page?
    pass
