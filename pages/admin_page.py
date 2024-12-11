from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//h6[contains(.,'Dashboard')]")
        self.admin_sidebarmenu =(By.XPATH, "(//span[contains(.,'Admin')])[1]") 
        self.user_management_submenu_title = (By.XPATH, "//h6[contains(.,'User Management')]")

    def validate_successful_login(self):
        self.wait_element_appears(self.title_page)
       
    def goToAdminPage(self):
        self.click_abstract(self.admin_sidebarmenu)

    def validate_user_management_submenu(self):
        self.wait_element_appears(self.user_management_submenu_title)

        