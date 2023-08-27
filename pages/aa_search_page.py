import time

from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def trip_type(self, trip_type):
        if trip_type == "one_way":
            one = self.driver.find_element(By.XPATH, "(//span[@class='control'])[3]")  # found myself
            one.click()
        if trip_type == "round_trip":
            one = self.driver.find_element(By.XPATH, "(//span[@class='control'])[2]")  # found myself
            one.click()

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
