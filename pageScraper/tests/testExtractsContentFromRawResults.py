from django.test import TestCase
from pageScraper.lib.extractsContentFromRawResults import ExtractsContentFromRawResults, HeaderNotFoundError, ResultsNotFoundError


class TestExtractsContentFromRawResults(TestCase):
  def setUp(self):
    self.rawResultsLines = [
      'Place Bib    Name     ', 
      '===== ======== ====== ', 
      '1     123     Joe     ', 
      '2     456     Bill    ', 
      '2/02/2010 - 10:20 am  ', 
    ]
    self.breakPoints = [5, 14]
    self.subject = ExtractsContentFromRawResults(self.rawResultsLines, self.breakPoints)
    self.degenerateSubject = ExtractsContentFromRawResults([''], [])

  def test_it_can_find_header_line(self):
    headerLine = self.subject.findHeaderLine()
    assert headerLine == 'Place Bib    Name     '

  def test_it_raises_exception_when_header_line_not_found(self):
    with self.assertRaises(HeaderNotFoundError):
      self.degenerateSubject.findHeaderLine()

  def test_it_can_find_result_lines(self):
    resultLines = self.subject.findResultLines()
    assert resultLines == [
      '1     123     Joe     ',
      '2     456     Bill    ',
    ]

  def test_it_raises_exception_when_result_lines_not_found(self):
    with self.assertRaises(ResultsNotFoundError):
      self.degenerateSubject.findResultLines()

  def test_extracts_headers(self):
    headers = self.subject.extractHeaders()
    assert headers == ['Place', 'Bib', 'Name']

  def test_extracts_results(self):
    results = self.subject.extractResults()
    assert results == [ ['1', '123', 'Joe'], ['2', '456', 'Bill'] ]
