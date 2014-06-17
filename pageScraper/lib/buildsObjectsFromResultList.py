from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject


class BuildsObjectsFromResultList(object):
  def __init__(self, the_class):
    self.the_class = the_class

  def build(self, resultList, attributeMapping):
    objects = []
    for result in resultList:
      objects.append(self.buildInstance(result, attributeMapping))
    return objects

  def buildInstance(self, result, attributeMapping):
    attributes = {}
    for attribute in attributeMapping:
      resultIndex = attributeMapping.get(attribute)
      attributes[attribute] = result[resultIndex]
    return FindsOrCreatesObject(self.the_class).findOrCreate(attributes)
      
