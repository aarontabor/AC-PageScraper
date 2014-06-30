from django.test import TestCase
from pageScraper.lib.extractsContentFromRawHeaders import ExtractsContentFromRawHeaders


class TestExtractsContentFromRawHeaders(TestCase):
  def setUp(self):
    self.correctlyFormattedLines = [
      ' ',
      'Testy Ten K (10 k)',
      'TestLand, NB June 22nd, 2014 Weather: Sunny 23C',
      'Race Director: Timmy Test',
    ]

    self.openingPreTagLines = [
      '<pre> Testy Ten K (10 k)',
    ]

    self.noBracketsAroundEventTypeLines = [
      ' ',
      'Testy Ten K 10 k',
    ]

    self.invalidMonthLines = [
      ' ',
      'Testy Ten K (10 k)',
      'TestLand, NB Gune 22nd, 2014 Weather: Sunny 23C',
    ]

    self.noSemiColonForRaceDirectorLines = [
      ' ',
      'Race Director Timmy Test',
    ]

    self.noLabelForRaceDirectorLines = [
      ' ',
      'Timmy Test',
    ]

  def test_extracts_racename_when_brackets_exist(self):
    raceName = ExtractsContentFromRawHeaders(self.correctlyFormattedLines).extractRaceName()
    assert raceName == 'Testy Ten K'

  def test_extract_racename_doesnt_include_opening_pre_tag(self):
    raceName = ExtractsContentFromRawHeaders(self.openingPreTagLines).extractRaceName()
    assert raceName == 'Testy Ten K'

  def test_extracts_first_full_line_as_fallback_for_racename(self):
    raceName = ExtractsContentFromRawHeaders(self.noBracketsAroundEventTypeLines).extractRaceName()
    assert raceName == 'Testy Ten K 10 k'

  def test_extracts_eventname_when_brackets_exist(self):
    eventName = ExtractsContentFromRawHeaders(self.correctlyFormattedLines).extractEventName()
    assert eventName == '10 k'

  def test_extracts_first_full_line_as_fallback_for_eventname(self):
    eventName = ExtractsContentFromRawHeaders(self.noBracketsAroundEventTypeLines).extractEventName()
    assert eventName == 'Testy Ten K 10 k'

  def test_extracts_location_when_valid_month_in_date(self):
    location = ExtractsContentFromRawHeaders(self.correctlyFormattedLines).extractLocation()
    assert location == 'TestLand, NB'

  def test_extracts_second_full_line_as_fallback_for_location(self):
    location = ExtractsContentFromRawHeaders(self.invalidMonthLines).extractLocation()
    assert location == 'TestLand, NB Gune 22nd, 2014 Weather: Sunny 23C'

  def  test_extracts_date_when_standard_format(self):
    # standard format is <month> <day>, <year>
    date = ExtractsContentFromRawHeaders(self.correctlyFormattedLines).extractDate()
    assert date == 'June 22nd, 2014'

  def  test_extracts_second_full_line_as_fallback_for_date(self):
    date = ExtractsContentFromRawHeaders(self.invalidMonthLines).extractDate()
    assert date == 'TestLand, NB Gune 22nd, 2014 Weather: Sunny 23C'

  def test_extracts_racedirector_when_prefixed_by_label_wo_semicolon(self):
    raceDirector = ExtractsContentFromRawHeaders(self.correctlyFormattedLines).extractRaceDirector()
    assert raceDirector == 'Timmy Test'

  def test_extracts_racedirector_when_prefixed_by_label_with_semicolon(self):
    raceDirector = ExtractsContentFromRawHeaders(self.noSemiColonForRaceDirectorLines).extractRaceDirector()
    assert raceDirector == 'Timmy Test'

  def test_fallback_to_empty_string_when_racedirector_not_prefixed(self):
    raceDirector = ExtractsContentFromRawHeaders(self.noLabelForRaceDirectorLines).extractRaceDirector()
    assert raceDirector == ''

