from django.test import TestCase
from pageScraper.lib.handlesBreakPoints import HandlesBreakPoints


class TestHandlesBreakPoints(TestCase):
  def setUp(self):
    self.subject = HandlesBreakPoints()

  def test_it_picks_the_right_line_when_equal_sign(self):
    rawResultsLines = [
      u'=================',
      u'Place Bib Name   ',
      u'===== === =======',
    ]
    breakLine = self.subject.findBreakLine(rawResultsLines)
    assert breakLine == u'===== === ======='

  def test_it_picks_The_right_line_when_dashes(self):
    rawResultsLines = [
      u'-----------------',
      u'Place Bib Name   ',
      u'----- --- -------',
    ]
    breakLine = self.subject.findBreakLine(rawResultsLines)
    assert breakLine == u'----- --- -------'

  def test_it_computes_the_correct_breakpoints(self):
    breakPointLine = u'===== == == '
    breakPoints = self.subject.computeBreakPointsFromLine(breakPointLine)
    assert breakPoints == [5, 8, 11]
    breakPointLine = u'----- -- --'
    breakPoints = self.subject.computeBreakPointsFromLine(breakPointLine)
    assert breakPoints == [5, 8]

  def test_it_can_split_a_line_on_break_points(self):
    #       ====   ========== ====
    line = u'This    line is  split'
    normal_point = 4
    runOver_point = 17
    outOfBounds_point = 22
    breakPoints = [normal_point, runOver_point, outOfBounds_point]
    result = self.subject.splitOnBreakPoints(line, breakPoints)
    assert result == [u'This', u'line is', u'split']
