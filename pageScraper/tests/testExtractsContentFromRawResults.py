from django.test import TestCase
from pageScraper.lib.extractsContentFromRawResults import ExtractsContentFromRawResults


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

  def test_extracts_headers(self):
    headers = self.subject.extractHeaders()
    assert headers == ['Place', 'Bib', 'Name']

  def test_extracts_results(self):
    results = self.subject.extractResults()
    assert results == [ ['1', '123', 'Joe'], ['2', '456', 'Bill'] ]
