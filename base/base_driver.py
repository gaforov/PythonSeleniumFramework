from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver, wait):
        self.wait = wait
        self.driver = driver

    def wait_for_presence_of_element(self, locator_type, locator):
        # wait = WebDriverWait(self.driver, 40)   # use if function is used with wait.
        return self.wait.until(EC.presence_of_element_located((locator_type, locator)))

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        return self.wait.until(EC.presence_of_all_elements_located((locator_type, locator)))

    def wait_until_element_is_clickable(self, locator_type, locator):
        return self.wait.until(EC.presence_of_element_located((locator_type, locator)))
