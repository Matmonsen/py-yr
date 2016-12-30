import unittest

from py_yr.config.settings import FORECAST_TYPE_HOURLY, FORECAST_TYPE_STANDARD
from py_yr.weatherdata import WeatherData
from py_yr.yr import Yr


class YrTestCase(unittest.TestCase):
    def setUp(self):
        self.lang_en = "en"
        self.lang_nb = "nb"
        self.lang_nn = "nn"
        self.invalid_language = "ru"

        self.forecast_type_hourly = FORECAST_TYPE_HOURLY
        self.forecast_type_standard = FORECAST_TYPE_STANDARD
        self.invalid_forecast_type = "invalid"

        self.location_special_case = "norge/oslo/oslo"
        self.invalid_location = "norge/hordaland/bergen/coruscant"
        self.valid_location_3_param = "spain/catalonia/barcelona/"
        self.valid_location_4_params = "norge/hordaland/bergen/bønes"

    def test_not_valid_url(self):
        yr = Yr(self.invalid_location)
        yr.download()
        self.assertIsNone(yr.source_data)

    def test_valid_url_3_params(self):
        yr = Yr(self.valid_location_3_param)
        yr.download()
        self.assertIsNotNone(yr.source_data)

    def test_valid_url_4_params(self):
        yr = Yr(self.valid_location_4_params)
        yr.download()
        self.assertIsNotNone(yr.source_data)

    def test_valid_url_with_special_case(self):
        yr = Yr(self.location_special_case)
        yr.download()
        self.assertIsNone(yr.source_data)

    def test_get_as_dict_with_3_params(self):
        yr = Yr(self.valid_location_3_param)
        yr.download()
        self.assertTrue(type(yr.get_as__dict()) is dict)

    def test_get_as_object_with_3_params(self):
        yr = Yr(self.valid_location_3_param)
        yr.download()
        self.assertTrue(type(yr.get_as_object()) is WeatherData)

    def test_get_as_xml_with_3_params(self):
        yr = Yr(self.valid_location_3_param)
        yr.download()
        self.assertTrue(type(yr.get_as_xml()) is str)

    def test_get_as_dict_with_4_params(self):
        yr = Yr(self.valid_location_4_params)
        yr.download()
        self.assertTrue(type(yr.get_as__dict()) is dict)

    def test_get_as_object_with_4_params(self):
        yr = Yr(self.valid_location_4_params)
        yr.download()
        self.assertTrue(type(yr.get_as_object()) is WeatherData)

    def test_get_as_xml_with_4_params(self):
        yr = Yr(self.valid_location_4_params)
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

    def test_language_en(self):
        yr = Yr(self.valid_location_4_params, self.lang_en)
        yr.download()
        self.assertIsNotNone(yr.get_as_xml())

    def test_language_nn(self):
        yr = Yr(self.valid_location_4_params, self.lang_nn)
        yr.download()
        self.assertIsNotNone(yr.get_as_xml())

    def test_language_nb(self):
        yr = Yr(self.valid_location_4_params, self.lang_nb)
        yr.download()
        self.assertIsNotNone(yr.get_as_xml())

    def test_language_invalid(self):
        yr = Yr(self.valid_location_4_params, self.invalid_language)
        yr.download()
        self.assertIsNone(yr.get_as_xml())

    def test_forecast_type_standard(self):
        yr = Yr(self.valid_location_4_params, forecast_type=self.forecast_type_standard)
        yr.download()
        self.assertIsNotNone(yr.get_as_xml())

    def test_forecast_type_hourly(self):
        yr = Yr(self.valid_location_4_params, forecast_type=self.forecast_type_hourly)
        yr.download()
        self.assertIsNotNone(yr.get_as_xml())

    def test_invalid_forecast_type(self):
        yr = Yr(self.valid_location_4_params, forecast_type=self.invalid_forecast_type)
        yr.download()
        self.assertIsNone(yr.get_as_xml())