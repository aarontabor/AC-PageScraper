from django.test import TestCase
from pageScraper.models import Runner
from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject


class TestFindsOrCreatesObject(TestCase):

    def setUp(self):
        self.subject = FindsOrCreatesObject(Runner)

        self.the_saved = Runner()
        self.the_saved.firstName = 'Tim'
        self.the_saved.lastName = 'Test'
        self.the_saved.save()

    def test_it_retrives_a_matching_object(self):
        attributesDict = {'firstName': 'Tim', 'lastName': 'Test'}
        the_returned = self.subject.findOrCreate(attributesDict)
        self.assertEqual(self.the_saved, the_returned)

    def test_it_creates_new_when_no__match_exists(self):
        attributesDict = {'firstName': 'John', 'lastName': 'Fake'}
        the_returned = self.subject.findOrCreate(attributesDict)
        self.assertNotEqual(self.the_saved, the_returned)
        self.assertEqual(the_returned.firstName, 'John')
