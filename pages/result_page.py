from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_stops(self):
        stops = self.wait.until(EC.presence_of_element_located((By.ID, "btn-stops-filter")))
        # stops = self.driver.find_element(By.ID, "//div[@class='search-result-item']")
        stops.click()
        non_stop = self.driver.find_element(By.XPATH, "(//span[@class='input-control'])[1]")
        non_stop.click()
        done_button = self.driver.find_element(By.CLASS_NAME, "done-button")
        done_button.click()
        flights_list = self.driver.find_elements(By.XPATH, "//*[@id='nonstop']")
        total_flights = len(flights_list)
        print("Total available non-stop flights:", total_flights)



