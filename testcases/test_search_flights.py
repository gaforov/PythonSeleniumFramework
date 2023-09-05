import pytest
from pages.search_page import SearchPage
import logging
from ddt import ddt, data, unpack

logging.basicConfig(level=logging.DEBUG, filename="test_logs.log")


# Add this argument in the logging: filemode="w" <--Override existing logs, filemode="a" <-- Append to an existing log


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter:
    @pytest.fixture(autouse=True)
    def objects_initializer(self):
        self.search_page = SearchPage(self.driver, self.wait)

    @data(
        ("LAX", "JFK", "09/05/2023", "one_way"),
        ("LAX", "SFO", "09/15/2023", "one_way"),
    )
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
        logging.debug("This is a sample log message")
        logging.info("This is a sample log message")
        logging.warning("This is a sample log message")
