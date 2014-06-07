import pytest

from handlesBreakPoints import HandlesBreakPoints
class TestHandlesBreakPoints:
  @pytest.fixture
  def subject(self):
    return HandlesBreakPoints()

  def test_it_picks_the_right_line(self, subject):
    rawResultsLines = [
      '=================',
      'Place Bib Name   ',
      '===== === =======',
    ]
    breakLine = subject.findBreakLine(rawResultsLines)
    assert breakLine == '===== === ======='

  def test_it_computes_the_correct_breakpoints(self, subject):
    breakPointLine = '===== == == '
    breakPoints = subject.computeBreakPointsFromLine(breakPointLine)
    assert breakPoints == [5, 8, 11]

    breakPointLine = '===== == =='
    breakPoints = subject.computeBreakPointsFromLine(breakPointLine)
    assert breakPoints == [5, 8]

  def test_it_can_split_a_line_on_break_points(self, subject):
    #       ====   ========== ====
    line = 'This    line is  split'
    breakPoints = [4, 17, 22]
    # first one - normal
    # second one - runs into next field (gotta back track)
    # third one - out of bounds

    result = subject.splitOnBreakPoints(line, breakPoints)
    assert result == ['This', 'line is', 'split']

