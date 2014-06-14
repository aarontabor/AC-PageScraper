class MapsPropertiesToObjects(object):
  def map(self, propertyDict, the_object):
    objectAttrs = the_object.__dict__.keys()
    for key in propertyDict.keys():
      if key not in objectAttrs:
        raise InvalidAttributeError
      the_object.__setattr__(key, propertyDict.get(key))
    return the_object

class InvalidAttributeError(Exception):
  pass
