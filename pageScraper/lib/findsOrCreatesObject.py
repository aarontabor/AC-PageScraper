from pageScraper.lib.mapsPropertiesToObjects import MapsPropertiesToObjects
class FindsOrCreatesObject(object):
        def __init__(self, the_class):
                self.the_class = the_class

        def findOrCreate(self, attributesDict):
                found = self.the_class.objects.filter(**attributesDict)
                if found:
                        return found[0]
                else:
                        toReturn = self.the_class()
                        MapsPropertiesToObjects().map(attributesDict, toReturn)
                        return toReturn
