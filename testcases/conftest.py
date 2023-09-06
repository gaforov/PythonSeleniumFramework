import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def setup(request, browser):
    service = Service()
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
        # driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=service)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=service)
    else:
        print('\nBrowser not supported')

    # Can create another if-else for envname if needed, such as; qa, dev, etc.
    # driver.get(URL to envname)

    wait = WebDriverWait(driver, 40)
    driver.get("https://www.aa.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    time.sleep(2)
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser')
    # parser.addoption('--envname')


@pytest.fixture(autouse=True, scope='class')
def browser(request):
    return request.config.getoption('--browser')


# @pytest.fixture(autouse=True, scope='class')
# def envname(request):
#     return request.config.getoption('--envname')
