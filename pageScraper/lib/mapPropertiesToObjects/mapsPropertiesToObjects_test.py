import pytest
from mapsPropertiesToObjects import MapsPropertiesToObjects, InvalidAttributeError

class Runner(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TestMapsPropertiesToObjects:
    def test_it_assigns_attributes(self):
        subject = MapsPropertiesToObjects()
        runner = Runner('Jim', 50)
        subject.map({'name':'Bill', 'age':35}, runner)
        assert runner.name is 'Bill'
        assert runner.age is 35

    def test_it_wont_create_new_attributes(self):
        subject = MapsPropertiesToObjects()
        runner = Runner('Jim', 50)
        with pytest.raises(InvalidAttributeError):
            subject.map({'fakeAttr':'boogity'}, runner)
