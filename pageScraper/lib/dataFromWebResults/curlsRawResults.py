from downloadsPageSource import DownloadsPageSource
from filtersRawResults import FiltersRawResults
class CurlsRawResults(object):
  def curl(self, url):
    downloader = DownloadsPageSource()
    filterer = FiltersRawResults()
    return filterer.filter(downloader.download(url))
