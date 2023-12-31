import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Utils


class ResultPage(BaseDriver):

    # Locators
    STOPS_BUTTON = "btn-stops-filter"
    NONSTOP_OPTION = "(//span[@class='input-control'])[1]"
    DONE_BUTTON = "done-button"
    NONSTOP_FLIGHTS_LIST = "//*[@id='nonstop']"
    NEW_SEARCH = "new-search-desktop"

    def get_nonstop_flights(self):
        """Create separate functions for other stops (1-stop, more stops, etc.)
           Combining them into a single function didn't seem to work efficiently."""
        self.wait.until(EC.presence_of_element_located((By.ID, self.STOPS_BUTTON))).click()  # 'stops' popup button
        self.driver.find_element(By.XPATH, self.NONSTOP_OPTION).click()  # Nonstop option radio btn
        self.driver.find_element(By.CLASS_NAME, self.DONE_BUTTON).click()

        # Verification/Validation part
        flights_list = self.driver.find_elements(By.XPATH, self.NONSTOP_FLIGHTS_LIST)  # List of Nonstop flights
        print("\nTotal available non-stop flights:", len(flights_list))

        utils = Utils()
        utils.assert_list_items_text(flights_list, "Nonstop")

        # Reset back to default search page, for new searches
        self.driver.get("https://www.aa.com/")

