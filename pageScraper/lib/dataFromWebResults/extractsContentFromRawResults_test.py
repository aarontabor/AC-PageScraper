from extractsContentFromRawResults import ExtractsContentFromRawResults
import pytest

class TestExtractsContentFromRawResults:
    @pytest.fixture
    def rawResultsLines(self):
        return [
                'Place Bib    Name     ',
                '===== ======== ====== ',
                '1     123     Joe     ',
                '2     456     Bill    ',
                '2/02/2010 - 10:20 am  ',
            ]

    @pytest.fixture
    def breakPoints(self):
        return [5, 14]

    def test_extracts_headers(self, rawResultsLines, breakPoints):
        subject = ExtractsContentFromRawResults(rawResultsLines, breakPoints)
        headers = subject.extractHeaders()
        assert headers == ['Place', 'Bib', 'Name']

    def test_extracts_results(self, rawResultsLines, breakPoints):
        subject = ExtractsContentFromRawResults(rawResultsLines, breakPoints)
        results = subject.extractResults()
        assert results == [ ['1', '123', 'Joe'], ['2', '456', 'Bill'] ]
