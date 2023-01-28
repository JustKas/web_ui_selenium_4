
import pytest
import pytest_html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as f_service
from selenium.webdriver.safari.service import Service as s_service

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.safari.options import Options as s_options
# from selenium.webdriver.common.keys import Keys
from time import sleep


# Fixture for Firefox
@pytest.fixture(scope="class")
def firefox_driver_init(request):
    ff_driver = webdriver.Firefox(service=f_service(GeckoDriverManager().install()))
    request.cls.driver = ff_driver
    yield
    ff_driver.quit()


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()


# Fixture for Safari
@pytest.fixture(scope="class")
def safari_driver_init(request):
    safari_driver = webdriver.Safari(service=s_service(), options=s_options())
    safari_driver.set_window_size(1920, 1080)
    safari_driver.delete_all_cookies()
    request.cls.driver = safari_driver
    yield
    safari_driver.quit()


@pytest.mark.usefixtures("firefox_driver_init")
class BasicFirefoxTest:
    pass


class TestUrlFirefox(BasicFirefoxTest):
    def test_open_url(self):
        exp_result = 'Xpath Practice Page | Shadow dom, nested shadow dom, iframe, ' \
                     'nested iframe and more complex automation scenarios.'
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        assert self.driver.title == exp_result

        sleep(1)


@pytest.mark.usefixtures("chrome_driver_init")
class BasicChromeTest:
    pass


class TestUrlChrome(BasicChromeTest):
    def test_open_url(self):
        exp_result = 'Xpath Practice Page | Shadow dom, nested shadow dom, iframe, ' \
                     'nested iframe and more complex automation scenarios.'
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        assert self.driver.title == exp_result
        sleep(1)


@pytest.mark.usefixtures("safari_driver_init")
class BasicSafariTest:
    pass


class TestUrlSafari(BasicSafariTest):
    def test_open_url(self):
        exp_result = 'Xpath Practice Page | Shadow dom, nested shadow dom, iframe, ' \
                     'nested iframe and more complex automation scenarios.'
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        assert self.driver.title == exp_result

        sleep(1)
# pytest --capture=no --verbose --html=pytest_selenium_test_report.html main.py
