from django.test import TestCase
from pageScraper.lib.curlsRawResults import CurlsRawResults

class TestCurlsRawResults(TestCase):
    def test_plumbing(self):
        subject = CurlsRawResults()
        result = subject.curl('http://www.google.com')
        assert isinstance(result, list)
