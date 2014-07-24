from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject
from pageScraper.lib.mapsPropertiesToObjects import MapsPropertiesToObjects
from pageScraper.models import Result


class FindsOrCreatesResult(object):
  def findOrCreate(self, attributeDict):
    result = FindsOrCreatesObject(Result).findOrCreate({
      'runner': attributeDict.get('runner'),
      'event': attributeDict.get('event'),
    })
    return MapsPropertiesToObjects().map(attributeDict, result)
