from curlsRawResults import CurlsRawResults

class TestCurlsRawResults:
    def test_plumbing(self):
        subject = CurlsRawResults()
        result = subject.curl('http://www.google.com')
        assert isinstance(result, list)
