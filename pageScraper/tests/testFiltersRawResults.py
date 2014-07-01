from django.test import TestCase
from pageScraper.lib.filtersRawResults import FiltersRawResults


class TestFiltersRawResults(TestCase):
  def setUp(self):
    self.subject = FiltersRawResults()
    self.sourceHtmlList = [
      '<html>', 
      'outside pre tag', 
      '<pre>', 
      'inside pre tag', 
      '</pre>', 
      '</html>', 
    ]

  def test_preserves_content_in_pre_tags(self):
    result = self.subject.filter(self.sourceHtmlList)
    assert u'<pre>' in result
    assert u'inside pre tag' in result
    assert u'</pre>' in result
    for line in result:
      assert isinstance(line, unicode)

  def test_filters_content_outside_pre_tags(self):
    result = self.subject.filter(self.sourceHtmlList)
    assert u'outside pre tag' not in result
    for line in result:
      assert isinstance(line, unicode)
