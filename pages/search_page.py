import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.flights_result_page import ResultPage
from utilities.utils import Utils


class SearchPage(BaseDriver):
    log = Utils.test_logger()
    # def __init__(self, driver, wait):
    #     super().__init__(driver, wait)
    #     self.driver = driver
    #     self.wait = wait

    # Locators
    DEPART_FROM_FIELD = "reservationFlightSearchForm.originAirport"
    DESTINATION = "reservationFlightSearchForm.destinationAirport"
    DEPART_DATE = "aa-leavingOn"
    RETURN_DATE = "aa-returningOn"
    SEARCH_BUTTON = "flightSearchForm.button.reSubmit"
    ONE_WAY_FLIGHT = "(//span[@class='control'])[3]"
    ROUND_TRIP_FLIGHT = "(//span[@class='control'])[2]"

    def trip_type(self, trip_type):
        match trip_type:
            case "one_way":
                self.driver.find_element(By.XPATH, self.ONE_WAY_FLIGHT).click()
            case "round_trip":
                self.driver.find_element(By.XPATH, self.ROUND_TRIP_FLIGHT).click()
            case _:
                return "Please enter 'one_way' or 'round_trip'"

    def search_flight(self, depart_airport, destination_airport, departure_date):
        depart_from = self.driver.find_element(By.ID, self.DEPART_FROM_FIELD)
        depart_from.clear()
        depart_from.send_keys(depart_airport)

        destination = self.driver.find_element(By.ID, self.DESTINATION)
        destination.clear()
        destination.send_keys(destination_airport)

        depart_date = self.driver.find_element(By.ID, self.DEPART_DATE)
        depart_date.clear()
        depart_date.send_keys(departure_date)
        time.sleep(2)

        search_button = self.driver.find_element(By.ID, self.SEARCH_BUTTON)
        search_button.click()

    # Another way to write search flights - divide into more independent smaller functions, below:

    def get_depart_from_field(self):
        return self.wait_until_element_is_clickable(By.ID, self.DEPART_FROM_FIELD)

    def enter_depart_airport(self, depart_airport):
        self.get_depart_from_field().clear()
        self.get_depart_from_field().send_keys(depart_airport)
        # self.get_depart_from_field().send_keys(Keys.RETURN) # sometimes needed depending on the field implementation

    def get_destination_field(self):
        return self.driver.find_element(By.ID, self.DESTINATION)

    def enter_destination_airport(self, destination_airport):
        self.get_destination_field().clear()
        self.get_destination_field().send_keys(destination_airport)
        # self.get_destination_field().send_keys(Keys.RETURN) # sometimes needed depending on the field implementation

    def get_departure_date(self):
        return self.driver.find_element(By.ID, self.DEPART_DATE)

    def enter_departure_date(self, departure_date):
        self.get_departure_date().clear()
        self.get_departure_date().send_keys(departure_date)
        # self.get_departure_date().send_keys(Keys.RETURN) # sometimes needed depending on the field implementation

    def get_return_date(self):
        return self.driver.find_element(By.ID, self.RETURN_DATE)

    def enter_return_date(self, return_date):
        self.get_return_date().clear()
        self.get_return_date().send_keys(return_date)

    def get_search_button(self):
        return self.driver.find_element(By.ID, self.SEARCH_BUTTON)

    def click_search_flight_button(self):
        self.get_search_button().click()

    def search_flights(self, depart_airport, destination_airport, departure_date, trip_type):
        self.enter_depart_airport(depart_airport)
        self.enter_destination_airport(destination_airport)
        self.enter_departure_date(departure_date)
        self.trip_type(trip_type)
        self.click_search_flight_button()
        result_page = ResultPage(self.driver, self.wait)
        return result_page
