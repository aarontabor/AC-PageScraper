from django.test import TestCase
from pageScraper.models import Runner
from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject


class TestFindsOrCreatesObject(TestCase):
  def setUp(self):
    self.subject = FindsOrCreatesObject(Runner)
    self.the_saved = Runner()
    self.the_saved.name = 'Tim'
    self.the_saved.save()

  def test_it_retrives_a_matching_object(self):
    attributesDict = {'name': 'Tim'}
    the_returned = self.subject.findOrCreate(attributesDict)
    self.assertEqual(self.the_saved, the_returned)

  def test_it_creates_new_when_no_match_exists(self):
    attributesDict = {'name': 'John'}
    the_returned = self.subject.findOrCreate(attributesDict)
    self.assertNotEqual(self.the_saved, the_returned)
    self.assertEqual(the_returned.name, 'John')
