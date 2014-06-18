from urllib import urlopen


class DownloadsPageSource(object):
  def download(self, url):
    try:
      sourceLines = urlopen(url).readlines()
      return sourceLines
    except IOError:
      raise CantDownloadError

class CantDownloadError(Exception):
  pass
