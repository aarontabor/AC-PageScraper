from django.test import TestCase
from pageScraper.models import Runner, Event, Result, Race
from pageScraper.lib.findsOrCreatesResult import FindsOrCreatesResult


class TestFindsOrCreatesResult(TestCase):
  def setUp(self):
    self.result = self.buildResult()
    self.resultFinder = FindsOrCreatesResult()

  def buildResult(self):
    runner = Runner()
    runner.save()
    race = Race()
    race.date = '2014-07-12'
    race.save()
    event = Event()
    event.race = race
    event.save()

    result = Result()
    result.runner = runner
    result.event = event
    result.position = '1'
    result.bib = '100'
    result.save()
    return result

  def test_it_retrieves_when_runner_and_event_match(self):
    the_returned = self.resultFinder.findOrCreate({
      'runner': self.result.runner,
      'event': self.result.event,
    })
    self.assertEqual(self.result.id, the_returned.id)

  def test_other_fields_are_updated_on_match(self):
    the_returned = self.resultFinder.findOrCreate({
      'runner': self.result.runner,
      'event': self.result.event,
      'bib': 50,
    })
    self.assertEqual(50, the_returned.bib)

  def test_it_creates_when_runner_doesnt_match(self):
    the_returned = self.resultFinder.findOrCreate({
      'runner': Runner(),
      'event': self.result.event,
    })
    self.assertNotEqual(self.result.id, the_returned.id)

  def test_it_creates_when_event_doesnt_match(self):
    the_returned = self.resultFinder.findOrCreate({
      'runner': self.result.runner,
      'event': Event(),
    })
    self.assertNotEqual(self.result.id, the_returned.id)
    
  def test_other_fields_are_preserved_on_create(self):
    the_returned = self.resultFinder.findOrCreate({
      'runner': Runner(),
      'event': Event(),
      'bib': 50,
    })
    self.assertEqual(50, the_returned.bib)
