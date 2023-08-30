import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Utils


class ResultPage(BaseDriver):
    # def __init__(self, driver, wait):
    #     super().__init__(driver, wait)
    #     self.driver = driver
    #     self.wait = wait

    # Locators
    STOPS_BUTTON = "btn-stops-filter"
    NONSTOP_OPTION = "(//span[@class='input-control'])[1]"
    DONE_BUTTON = "done-button"
    NONSTOP_FLIGHTS_LIST = "//*[@id='nonstop']"

    def filter_nonstop_flights(self):
        """Create separate functions for other stops (1-stop, more stops, etc.)
           Combining them into a single function didn't seem to work efficiently."""
        self.wait.until(EC.presence_of_element_located((By.ID, self.STOPS_BUTTON))).click()  # stops popup button
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.NONSTOP_OPTION).click()  # Nonstop option radio btn
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, self.DONE_BUTTON).click()

# Verification/Validation part
        flights_list = self.driver.find_elements(By.XPATH, self.NONSTOP_FLIGHTS_LIST)  # List of Nonstop flights
        total_flights = len(flights_list)
        print("\nTotal available non-stop flights:", total_flights)

        # This part is moved to utilities package. Instead, call from Utils class.
        # increment = 1
        # for stop in flights_list:
        #     print("Type of flight is:", stop.text)
        #     assert stop.text == "Nonstop"
        #     print("(Test", increment, "of", total_flights, ") Passed!")
        #     increment += 1

        utils = Utils()
        utils.assert_list_items_text(flights_list, "Nonstop")


