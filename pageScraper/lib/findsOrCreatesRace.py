from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject
from pageScraper.lib.mapsPropertiesToObjects import MapsPropertiesToObjects
from pageScraper.models import Race


class FindsOrCreatesRace(object):
  def findOrCreate(self, attributeDict):
    race = FindsOrCreatesObject(Race).findOrCreate({
      'name': attributeDict.get('name'),
      'date': attributeDict.get('date'),
    })
    return MapsPropertiesToObjects().map(attributeDict, race)
