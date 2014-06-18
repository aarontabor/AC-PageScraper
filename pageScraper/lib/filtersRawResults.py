class FiltersRawResults(object):
  def filter(self, sourceHtmlList):
    filteredLines = []
    inPre = False
    for line in sourceHtmlList:
      if '</pre' in line:
        inPre = False
      if inPre:
        filteredLines.append(unicode(line, errors='replace'))
      if '<pre' in line:
        inPre = True
    return filteredLines
