from django.test import TestCase
from pageScraper.lib.mapsPropertiesToObjects import MapsPropertiesToObjects


class Runner(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

class TestMapsPropertiesToObjects(TestCase):
  def test_it_assigns_attributes(self):
    subject = MapsPropertiesToObjects()
    runner = Runner('Jim', 50)
    subject.map({'name':'Bill', 'age':35}, runner)
    assert runner.name is 'Bill'
    assert runner.age is 35
