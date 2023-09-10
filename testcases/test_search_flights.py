import unittest

import pytest
from ddt import ddt, file_data, data, unpack

from pages.search_page import SearchPage
from utilities.utils import Utils


# logging.basicConfig(level=logging.DEBUG, filename="test_logs.log")

# Add this argument in the logging: filemode="w" <--Override existing logs, filemode="a" <-- Append to an existing log


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objects_initializer(self):
        self.search_page = SearchPage(self.driver, self.wait)

    # DDT Examples:
    # Example 1: In-line data passed directly
    # @data(("LAX", "JFK", "09/05/2023", "one_way"),
    #       ("LAX", "SFO", "09/15/2023", "one_way")
    #       )  # more than one data is failing, because after each test, the browser is not restarting.
    # @unpack

    # Example 2: Reading from json or yaml files.
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testdata.yaml")

    # Example 3: Reading from an Excel/csv file.
    @data(*Utils.read_data_from_excel_file("/Users/saidgaforov/PycharmProjects/PythonSeleniumFramework/testdata/excel_file.xlsx", "Sheet1"))
    @unpack
    def test_search_flights(self, depart_from, destination, departure_date, trip_type):
        # search_page.trip_type("one_way")  # use only "one_way" or "round_trip" as arguments
        # search_page.search_flight("LAX", "JFK", "09/05/2023")

        # Or use second function from the same class (SearchPage)
        # search_result_page = self.search_page.search_flights("LAX", "JFK", "09/05/2023", "one_way")
        search_result_page = self.search_page.search_flights(depart_from, destination, departure_date, trip_type)

        '''These two lines below are replaced by the above line. 
        .search_flights() function returns Result Page, no need to create its object again. '''
        # result_page = ResultPage(self.driver, self.wait)
        # result_page.filter_nonstop_flights()
        search_result_page.get_nonstop_flights()
        # logging.debug("This is a sample log message")
        # logging.info("This is a sample log message")
        # logging.warning("This is a sample log message")
