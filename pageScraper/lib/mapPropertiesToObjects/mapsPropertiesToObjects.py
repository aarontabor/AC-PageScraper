class MapsPropertiesToObjects(object):
  def map(self, propertyDict, object):
    objectAttrs = object.__dict__.keys()
    for key in propertyDict.keys():
      if key not in objectAttrs:
        raise InvalidAttributeError
      object.__setattr__(key, propertyDict.get(key))

class InvalidAttributeError(Exception):
  pass
