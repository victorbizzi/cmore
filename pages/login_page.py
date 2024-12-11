from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from utilities.globalVars import globalVars


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.XPATH,  "//div[2]/input")
        self.password_field = (By.XPATH,  "//div[2]/div/div[2]/input")
        self.login_btn = (By.XPATH,  "//button[contains(.,'Login')]")        
        self.error_login_message = (By.XPATH, "//h3")
        self.x_icon_user = (By.CSS_SELECTOR, ".form_group:nth-child(1) path")
        self.x_icon_password = (By.CSS_SELECTOR, ".form_group:nth-child(2) path")

    def perform_login(self, user, password):
        self.sendkeys_abstract(self.username_field, user)
        self.sendkeys_abstract(self.password_field, password)
        self.click_abstract(self.login_btn)

    def perform_valid_login(self):
        self.sendkeys_abstract(self.username_field, globalVars.user)
        self.sendkeys_abstract(self.password_field, globalVars.password)
        self.click_abstract(self.login_btn)

    def validate_error_login_msg(self):
        self.validate_if_element_exists(self.error_login_message)

    def validate_error_login(self, expected_message):
        text_found =  self.validate_element_text(self.error_login_message)
        assert text_found == expected_message, f"Returned message was: '{text_found}', but the expected is: '{expected_message}'."

    def wait_elements_load(self):
        self.wait_element_appears(self.username_field)
        self.wait_element_appears(self.password_field)
        