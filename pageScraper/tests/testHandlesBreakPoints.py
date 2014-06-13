from django.test import TestCase
from pageScraper.lib.handlesBreakPoints import HandlesBreakPoints


class TestHandlesBreakPoints(TestCase):
    def setUp(self):
        self.subject = HandlesBreakPoints()

    def test_it_picks_the_right_line(self):
        rawResultsLines = [
                '=================', 
                'Place Bib Name   ', 
                '===== === =======', 
                ]
        breakLine = self.subject.findBreakLine(rawResultsLines)
        assert breakLine == '===== === ======='

    def test_it_computes_the_correct_breakpoints(self):
        breakPointLine = '===== == == '
        breakPoints = self.subject.computeBreakPointsFromLine(breakPointLine)
        assert breakPoints == [5, 8, 11]

        breakPointLine = '===== == =='
        breakPoints = self.subject.computeBreakPointsFromLine(breakPointLine)
        assert breakPoints == [5, 8]

    def test_it_can_split_a_line_on_break_points(self):
        #       ====   ========== ====
        line = 'This    line is  split'
        normal_point = 4
        runOver_point = 17
        outOfBounds_point = 22
        breakPoints = [normal_point, runOver_point, outOfBounds_point]

        result = self.subject.splitOnBreakPoints(line, breakPoints)
        assert result == ['This', 'line is', 'split']

