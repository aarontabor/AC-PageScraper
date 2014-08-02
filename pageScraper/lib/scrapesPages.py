from curlsRawResults import CurlsRawResults
from extractsContentFromRawResults import ExtractsContentFromRawResults
from handlesBreakPoints import HandlesBreakPoints
from extractsContentFromRawHeaders import ExtractsContentFromRawHeaders


'''
This utility scrapes atlantic chip online results pages to carve out datastructures:
    - list of headers (Place, Bib, Name ...)
    - list of results (2D array, each element is a list corresponding to headers)
'''

class ScrapesPages(object):
  def __init__(self, url):
    self.url = url
    self.rawResultLines = CurlsRawResults().curl(self.url)
    self.breakPoints = HandlesBreakPoints().computeBreakPoints(self.rawResultLines)

  def scrapeHeaders(self):
    return ExtractsContentFromRawResults(self.rawResultLines, self.breakPoints).extractHeaders()

  def scrapeResults(self):
    return ExtractsContentFromRawResults(self.rawResultLines, self.breakPoints).extractResults()

  def scrapeRaceName(self):
    return ExtractsContentFromRawHeaders(self.rawResultLines).extractRaceName()

  def scrapeEventName(self):
    return ExtractsContentFromRawHeaders(self.rawResultLines).extractEventName()

  def scrapeLocation(self):
    return ExtractsContentFromRawHeaders(self.rawResultLines).extractLocation()

  def scrapeDate(self):
    return ExtractsContentFromRawHeaders(self.rawResultLines).extractDate()

  def scrapeRaceDirector(self):
    return ExtractsContentFromRawHeaders(self.rawResultLines).extractRaceDirector()

  def rawResultText(self):
    return ''.join(self.rawResultLines)
