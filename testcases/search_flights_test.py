import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from pages.search_page import SearchPage
from pages.result_page import ResultPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_flights(self):
        search_page = SearchPage(self.driver, self.wait)
        search_page.trip_type("one_way")  # use only "one_way" or "round_trip" as arguments
        search_page.search_flight("LAX", "JFK", "09/05/2023")

        result_page = ResultPage(self.driver, self.wait)
        result_page.filter_nonstop_flights()


