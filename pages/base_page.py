import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_element_abstract(self, locator):
        return self.driver.find_element(*locator)

    def find_multiple_elements_abstract(self, locator):
        self.wait_element_appears(locator)
        return self.driver.find_element(*locator)

    def sendkeys_abstract(self, locator, text):
        self.wait_element_appears(locator)
        self.find_element_abstract(locator).send_keys(text)

    def click_abstract(self, locator):
        self.wait_element_appears(locator)
        self.find_element_abstract(locator).click()

    def validate_if_element_exists(self, locator):
        self.wait_element_appears(locator)
        assert self.find_element_abstract(locator).is_displayed(), f"Element '{locator}' has been not found!"

    def validate_element_text(self, locator):
        self.wait_element_appears(locator)
        return self.find_element_abstract(locator).text

    def wait_element_appears(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def validate_if_element_exists(self, locator):
        return self.find_element_abstract(locator), f"Element '{locator}' does not exist but it should exist"

    def validate_if_element_does_not_exist(self, locator):
        assert len(self.find_element_abstract(locator)) == 0, f"Element '{locator}' does not exist but it should exist"

    def double_click_abstract(self, locator):
        element = self.wait_element_appears(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        element = self.wait_element_appears(locator)
        ActionChains(self.driver).context_click(element).perform()

    def press_keyboard_keys(self, locator, key):
        element = self.find_element_abstract(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "BACKSPACE":
            element.send_keys(Keys.BACKSPACE)
