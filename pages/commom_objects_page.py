from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CommonObjectsPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//h6[contains(.,'{pageName}}')]")
        self.sidebarmenu =(By.XPATH, "(//span[contains(.,'{menuName}')])[1]") 
        self.submenu_header_title = (By.XPATH, "//h6[contains(.,'{titlePage}}')]")
        self.toast_message = (By.XPATH, "//div[contains(.,'{message}')]")



# The idea of this common_objects+age is:
# Centralize elements that are repeated in other pages
# Using variables and placeholders (to facilitate the maintenance, simplify the development, and make
# allows for quick adjustments or enhancements as the project evolves







        