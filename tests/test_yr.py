import unittest

from py_yr.weatherdata import WeatherData
from py_yr.yr import Yr


class YrTestCase(unittest.TestCase):
    def setUp(self):
        self.lang_en = "en"
        self.lang_nb = "nb"
        self.lang_nn = "nn"

        self.forecast_type_hourly = "hourly"
        self.forecast_type_standard = "standard"

        self.location_special_case = "norge/oslo/oslo"
        self.invalid_location = "norge/hordaland/bergen/coruscant"
        self.valid_location = "norge/hordaland/bergen/bønes"

    def test_not_valid_url(self):
        yr = Yr(self.invalid_location)
        yr.download()
        self.assertIsNone(yr.source_data)

    def test_valid_url(self):
        yr = Yr(self.valid_location)
        yr.download()
        self.assertIsNotNone(yr.source_data)

    def test_valid_url_with_special_case(self):
        yr = Yr(self.location_special_case)
        yr.download()
        self.assertIsNone(yr.source_data)

    def test_get_as_dict(self):
        yr = Yr(self.valid_location)
        yr.download()
        self.assertTrue(type(yr.get_as__dict()) is dict)

    def test_get_as_object(self):
        yr = Yr(self.valid_location)
        yr.download()
        self.assertTrue(type(yr.get_as_object()) is WeatherData)

    def test_get_as_xml(self):
        yr = Yr(self.valid_location)
        yr.download()
        self.assertTrue(type(yr.get_as_xml()) is str)

    def test_get_as_dict_with_invalid_with_location(self):
        yr = Yr(self.invalid_location)
        yr.download()
        self.assertIsNone(yr.get_as__dict())

    def test_get_as_object_with_location(self):
        yr = Yr(self.invalid_location)
        yr.download()
        self.assertIsNone(yr.get_as_object())

    def test_get_as_xml_with_location(self):
        yr = Yr(self.invalid_location)
        yr.download()
        self.assertIsNone(yr.get_as_xml())