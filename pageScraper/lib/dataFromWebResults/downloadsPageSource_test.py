from downloadsPageSource import DownloadsPageSource, CantDownloadError
import pytest

class TestDownloadsPageSource:
    def test_it_returns_a_list_of_lines(self):
        subject = DownloadsPageSource()
        result = subject.download("http://www.google.com")
        assert isinstance(result, list)
    
    def test_raises_exception_on_error(self):
      subject = DownloadsPageSource()
      with pytest.raises(CantDownloadError):
        result = subject.download("hoogity.boogity.boomBoomBoom")

