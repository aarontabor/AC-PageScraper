from re import findall


class HandlesBreakPoints(object):
  def computeBreakPoints(self, rawResults):
    breakLine = self.findBreakLine(rawResults)
    breakPoints = self.computeBreakPointsFromLine(breakLine)
    return breakPoints

  def computeBreakPointsFromLine(self, breakPointLine):
    lineChars = list(breakPointLine)
    breaks = []
    count = 0
    inField = False
    for char in lineChars:
      if char ==  u'=':
        inField = True
      if inField and char == u' ':
        breaks.append(count)
        inField = False
      count += 1
    return breaks

  def findBreakLine(self, rawResultsLines):
    bannerLines = []
    for line in rawResultsLines:
      if findall(r'^\s*=', line):
        bannerLines.append(line)
    return bannerLines[1]

  def splitOnBreakPoints(self, line, breakPoints):
    delimieter=u'@'
    lineChars = list(line)
    for breakPoint in breakPoints:
      point = breakPoint
      if len(lineChars) > point:
        while lineChars[point] != u' ':
          point -= 1
        lineChars[point] = delimieter
    theLine = u''.join(lineChars)
    fields = theLine.split(delimieter)
    fields = [ field.strip() for field in fields ]
    return fields
