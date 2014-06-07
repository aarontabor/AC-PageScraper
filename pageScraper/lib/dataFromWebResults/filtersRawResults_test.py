import pytest 
from filtersRawResults import FiltersRawResults

class TestFiltersRawResults:
  @pytest.fixture
  def subject(self):
    return FiltersRawResults()

  @pytest.fixture
  def sourceHtmlList(self):
    return [ '<html>',
             'outside pre tag',
             '<pre>',
             'inside pre tag',
             '</pre>',
             '</html>',
          ]

  def test_preserves_content_in_pre_tags(self, subject, sourceHtmlList):
    result = subject.filter(sourceHtmlList)
    assert 'inside pre tag' in result

  def test_filters_content_outside_pre_tags(self, subject, sourceHtmlList):
    result = subject.filter(sourceHtmlList)
    assert 'outside pre tag' not in result
