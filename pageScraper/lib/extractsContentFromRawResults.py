from re import findall
from handlesBreakPoints import HandlesBreakPoints


uniqueHeaderIdentifier = 'Place'

class ExtractsContentFromRawResults(object):
  def __init__(self, rawResultsLines, breakPoints):
    self.rawResultLines = rawResultsLines
    self.breakPoints = breakPoints

  def extractHeaders(self):
    headerLine = self.findHeaderLine()
    return HandlesBreakPoints().splitOnBreakPoints(headerLine, self.breakPoints)
      
  def findHeaderLine(self):
    for line in self.rawResultLines:
      if uniqueHeaderIdentifier in line:
        return line
    raise HeaderNotFoundError

  def extractResults(self):
    resultLines = self.findResultLines()
    results = []
    handlesBreakPoints = HandlesBreakPoints()
    for line in resultLines:
      results.append(handlesBreakPoints.splitOnBreakPoints(line, self.breakPoints))
    return results


  def findResultLines(self):
    resultLines = []
    for line in self.rawResultLines:
      if findall(r'^\s*\d+', line):
        resultLines.append(line)
    if resultLines == []:
      raise ResultsNotFoundError
    return resultLines[:-1] # the last one is lmt

class HeaderNotFoundError(Exception):
  pass

class ResultsNotFoundError(Exception):
  pass
