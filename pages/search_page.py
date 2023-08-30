import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SearchPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.driver = wait

    def trip_type(self, trip_type):
        match trip_type:
            case "one_way":
                self.driver.find_element(By.XPATH, "(//span[@class='control'])[3]").click()
            case "round_trip":
                self.driver.find_element(By.XPATH, "(//span[@class='control'])[2]").click()
            case _:
                return "Please enter 'one_way' or 'round_trip'"

    def search_flight(self, depart_airport, destination_airport, departure_date):
        depart_from = self.driver.find_element(By.ID, "reservationFlightSearchForm.originAirport")
        depart_from.clear()
        depart_from.send_keys(depart_airport)
        destination = self.driver.find_element(By.ID, "reservationFlightSearchForm.destinationAirport")
        destination.clear()
        destination.send_keys(destination_airport)
        depart_date = self.driver.find_element(By.ID, "aa-leavingOn")
        depart_date.clear()
        depart_date.send_keys(departure_date)
        time.sleep(2)
        search_button = self.driver.find_element(By.ID, "flightSearchForm.button.reSubmit")
        search_button.click()
