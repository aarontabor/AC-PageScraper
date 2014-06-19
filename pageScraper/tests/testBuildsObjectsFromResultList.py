from django.test import TestCase
from pageScraper.models import Runner
from pageScraper.lib.buildsObjectsFromResultList import BuildsObjectsFromResultList


class TestBuildsObjectsFromResultList(TestCase):
  def setUp(self):
    self.subject = BuildsObjectsFromResultList(Runner)
    self.resultsList = [
      ['foo', 'Tim'],
      ['bar', 'John'],
    ]
    self.attributeMapping = {'name': 1}
    
  def test_it_builds_an_object_for_each_result(self):
    runners = self.subject.build(self.resultsList, self.attributeMapping) 

    self.assertEqual(2, len(runners))

  def test_it_maps_result_attributes_onto_objects(self):
    runners = self.subject.build(self.resultsList, self.attributeMapping)
    firstRunner = runners[0]

    self.assertEqual(firstRunner.name, 'Tim')

  def test_it_doesnt_map_non_attributes(self):
    runners = self.subject.build(self.resultsList, self.attributeMapping)
    firstRunner = runners[0]

    self.assertNotEqual(firstRunner.name, 'foo')

