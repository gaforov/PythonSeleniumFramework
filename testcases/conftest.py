import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    # service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 40)
    # driver.get("https://www.expedia.com/Flights")
    driver.get("https://www.aa.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    time.sleep(2)
    driver.close()
