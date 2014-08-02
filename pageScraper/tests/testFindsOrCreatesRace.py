from django.test import TestCase
from pageScraper.models import Race
from pageScraper.lib.findsOrCreatesRace import FindsOrCreatesRace


class TestFindsOrCreatesRace(TestCase):

  def setUp(self):
    self.race = Race(
        name='Test Race',
        date='2014-01-01',
        location='Place',
    )
    self.race.save()
    self.finder = FindsOrCreatesRace()

  def test_it_retrieves_when_name_and_date_match(self):
    retrievedRace = self.finder.findOrCreate({
      'name': 'Test Race',
      'date': '2014-01-01',
    })
    self.assertEquals(self.race.id, retrievedRace.id)

  def test_other_fields_are_updated_on_match(self):
    retrievedRace = self.finder.findOrCreate({
      'name': 'Test Race',
      'date': '2014-01-01',
      'location': 'Another Place',
    })
    self.assertEquals(self.race.id, retrievedRace.id)
    self.assertEquals('Another Place', retrievedRace.location)

  def test_it_creates_when_name_doesnt_match(self):
    retrievedRace = self.finder.findOrCreate({
      'name': 'Another Test Race',
      'date': '2014-01-01',
    })
    self.assertNotEquals(self.race.id, retrievedRace.id)

  def test_it_creates_when_date_doesnt_match(self):
    retrievedRace = self.finder.findOrCreate({
      'name': 'Test Race',
      'date': '2015-01-01',
    })
    self.assertNotEquals(self.race.id, retrievedRace.id)

  def test_other_fields_are_preserved_on_create(self):
    retrievedRace = self.finder.findOrCreate({
      'name': 'Another Test Race',
      'date': '2015-01-01',
      'location': 'Another Place',
    })
    self.assertNotEquals(self.race.id, retrievedRace.id)
    self.assertEquals('Another Place', retrievedRace.location)


