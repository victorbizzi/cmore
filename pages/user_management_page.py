from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from time import sleep


class UserManagement(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//h6[contains(.,'User Management')]")
        self.adduser_button = (By.XPATH,  "//button[contains(.,' Add')]")
        self.search_username = (By.XPATH, "//div[2]/input")
        self.search_um_button = (By.XPATH, "//button[contains(.,'Search')]") 
        self.first_grid_result = (By.XPATH, "//div[3]/div/div[2]/div/div/div[2]/div")       
        self.first_grid_result_edit_icon = (By.XPATH, "//button[2]/i")
        self.first_grid_result_delete_icon = (By.XPATH, "(//div[6]/div/button/i)[1]")
        self.save_button_um = (By.XPATH, "//button[contains(.,'Save')]")
        self.user_role_dropdown = (By.XPATH, "(//div/div/div/div[2]/div/div/div)[1]")
        self.user_role_admin = (By.XPATH, "//*[contains(text(), 'Admin')]")
        self.user_role_delete_confirmation_alert = (By.XPATH, "//p[contains(.,'Are you Sure?')]")
        self.user_role_delete_confirmation_button = (By.XPATH, "//button[contains(.,' Yes, Delete')]")
        self.toast_delete_message = (By.XPATH, "//div[contains(.,'Successfully Deleted')]")

    def searchUserByUserName(self, employee_username):
        sleep(15)
        self.wait_element_appears(self.search_username)
        self.sendkeys_abstract(self.search_username, employee_username)
        self.click_abstract(self.search_um_button)
        self.wait_element_appears(self.first_grid_result)
        

    def validate_um_page(self):
        self.wait_element_appears(self.title_page)
    
    def clickInAdd(self):
        self.click_abstract(self.adduser_button)

    def clickSearchButton(self):
        self.click_abstract(self.search_um_button)

    def editAdminUser(self):
        self.click_abstract(self.first_grid_result_edit_icon)
        self.changeUserRoleToAdmin()
        self.click_abstract(self.save_button_um)
        sleep(10)

    def changeUserRoleToAdmin(self):
        self.click_abstract(self.user_role_dropdown)
        self.click_abstract(self.user_role_admin)

    def deleteUser(self):
        self.click_abstract(self.first_grid_result_delete_icon)
        self.wait_element_appears(self.user_role_delete_confirmation_alert)
        self.click_abstract(self.user_role_delete_confirmation_button)  
        self.wait_element_appears(self.toast_delete_message)




    

        

