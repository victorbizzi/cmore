from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.globalVars import globalVars
from pages.pim_page import PimPage
import names
from time import sleep

class AddUser(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_add_user_page = (By.XPATH, "//h6[contains(.,'Add User')]")
        self.user_role_dropdown = (By.XPATH, "(//div/div/div/div/div[2]/div/div)[1]")
        self.user_employee_name = (By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input")
        self.user_status_dropdown = (By.XPATH, "(//div/div/div/div/div[2]/div/div)[3]")
        self.user_status_enabled = (By.XPATH, "//*[contains(text(), 'Enabled')]")
        self.user_username = (By.XPATH, "(//div/div/div/div/div[2]/div/div)[4]")
        self.user_role_admin = (By.XPATH, "//*[contains(text(), 'Admin')]")
        self.user_role_ess = (By.XPATH, "")

    def fillAddUserFields(self):
        firstName = self.generateRandomFirstName()
        lastName = self.generateRandomLastName()
        employeeName = firstName + " " + lastName
        self.wait_element_appears(self.title_add_user_page)
        self.selectUserRoleAdmin()        
        element = self.find_element_abstract(self.user_employee_name)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()        
        element.send_keys("Ra")
        dropdown_option = (By.XPATH, "//*[contains(text(), 'Virat')]")
        self.wait_element_appears(dropdown_option)
        self.driver.find_element(*dropdown_option).click()
        self.selectUserStatusEnabled()

    def selectUserRoleAdmin(self):
        self.click_abstract(self.user_role_dropdown)
        self.wait_element_appears(self.user_role_admin)
        self.click_abstract(self.user_role_admin)

    def generateRandomFirstName(self):
        return names.get_first_name()
    
    def generateRandomLastName(self):
        return names.get_last_name()
    
    def selectUserStatusEnabled(self):
        self.click_abstract(self.user_status_dropdown)
        self.wait_element_appears(self.user_status_enabled)
        self.click_abstract(self.user_status_enabled)    

    def addEmployeeFullSteps(self):
        login_page = LoginPage()
        home_page = HomePage()
        pim_page = PimPage()
        login_page.wait_elements_load()
        login_page.perform_login(globalVars.userName, globalVars.userPassword)
        home_page.validate_successful_login()
        pim_page.goToPimPage()
        pim_page.addEmployeeWithUsername()
        employee_username = pim_page.getEmployeeUsername()
        pim_page.clickSaveButton() 
        sleep(10)       
        return employee_username

