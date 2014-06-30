import re


class ExtractsContentFromRawHeaders(object):
  def __init__(self, rawLines):
    self.rawLines = rawLines
    self.monthPrefixes = 'jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec'
    

  def extractRaceName(self):
    raceName = self.findRaceName()
    if raceName:
      return raceName
    else:
      return self.fallbackRaceNameLine()

  def findRaceName(self):
    for line in self.rawLines:
      match = re.search(r'^\s*(<pre>){0,1}\s*(?P<racename>.*) \(.*\)', line)
      if match:
        return match.group('racename')
    return ''

  def fallbackRaceNameLine(self):
    return self.nthNonBlankLine(1)

  def nthNonBlankLine(self, n):
    count = 0
    for line in self.rawLines:
      if line.strip():
        count += 1
        if count == n:
          return line


  def extractEventName(self):
    eventName = self.findEventName()
    if eventName:
      return eventName
    else:
       return self.fallbackEventNameLine()

  def findEventName(self):
    for line in self.rawLines:
      match = re.search(r'.*\((?P<eventname>.*)\)', line)
      if match:
        return match.group('eventname')
    return ''

  def fallbackEventNameLine(self):
    return self.nthNonBlankLine(1)

  def extractLocation(self):
    location = self.findLocation()
    if location:
      return location
    else:
      return self.fallbackLocation()

  def findLocation(self):
    for line in self.rawLines:
      match = re.search(r'(?P<location>.*) (%s)' % self.monthPrefixes, line, re.IGNORECASE) 
      if match:
         return match.group('location')
    return ''

  def fallbackLocation(self):
    return self.nthNonBlankLine(2)

  def extractDate(self):
    date = self.findDate()
    if date:
      return date
    else:
      return self.fallbackDate()

  def findDate(self):
    for line in self.rawLines:
      match = re.search(r'(?P<monthprefix>%s)\w* (?P<date>\d+\w*), (?P<year>\d{4})' % self.monthPrefixes, line, re.IGNORECASE)
      if match:
        return match.group(0)
    return ''

  def fallbackDate(self):
    return self.nthNonBlankLine(2)

  def extractRaceDirector(self):
    raceDirector = self.findRaceDirector()
    if raceDirector:
      return raceDirector
    else:
      return self.fallbackRaceDirector()

  def findRaceDirector(self):
    for line in self.rawLines:
      match = re.search(r'Race Director[:]{0,1} (?P<name>[\w\s]+)', line)
      if match:
        return match.group('name')
    return ''

  def fallbackRaceDirector(self):
    return ''


