from pyshadow.main import Shadow
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_shadow_elem(self, parent_elem, css_locator: str) -> WebElement:
        shadow = Shadow(self.driver)
        return shadow.find_element(parent_elem, css_locator)
