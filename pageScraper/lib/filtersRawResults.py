class FiltersRawResults(object):
  def filter(self, sourceHtmlList):
    filteredLines = []
    inPre = False
    for line in sourceHtmlList:
      if '</pre' in line:
        inPre = False
      if inPre:
        filteredLines.append(line)
      if '<pre' in line:
        inPre = True
    return filteredLines
