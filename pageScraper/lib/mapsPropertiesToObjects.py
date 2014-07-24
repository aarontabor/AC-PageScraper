class MapsPropertiesToObjects(object):
  def map(self, propertyDict, the_object):
    for key in propertyDict.keys():
      the_object.__setattr__(key, propertyDict.get(key))
    return the_object
