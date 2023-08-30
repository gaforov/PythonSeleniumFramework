from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class ResultPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def filter_nonstop_flights(self):
        """Create separate functions for other stops (1-stop, more stops, etc.)
           Combining them into a single function didn't seem to work efficiently."""
        self.wait.until(EC.presence_of_element_located((By.ID, "btn-stops-filter"))).click()  # stops dropdown button
        self.driver.find_element(By.XPATH, "(//span[@class='input-control'])[1]").click()  # Nonstop option radio btn
        self.driver.find_element(By.CLASS_NAME, "done-button").click()  # Done button
        flights_list = self.driver.find_elements(By.XPATH, "//*[@id='nonstop']")  # List of Nonstop flights
        total_flights = len(flights_list)
        print("\nTotal available non-stop flights:", total_flights)
        increment = 1
        for stop in flights_list:
            print("Type of flight is:", stop.text)
            assert stop.text == "Nonstop"
            print("(Test", increment, "of", total_flights, ") Passed!")
            increment += 1
