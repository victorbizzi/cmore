from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
import names
import random
import string
from time import sleep


class PimPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.pim_sidebarmenu = (By.XPATH, "//span[contains(.,'PIM')]")
        self.pim_title = (By.XPATH, "//h6[contains(.,'PIM')]")
        self.add_employee_title = (By.XPATH, "//h6[contains(.,'Add Employee')]")
        self.add_employee_button = (By.XPATH, "//button[contains(.,' Add')]")
        self.employee_first_name = (By.XPATH, "(//div[2]/div/div[2]/input)[1]")
        self.employee_middle_name = (By.XPATH, "(//div[2]/div[2]/input)[1]")
        self.employee_last_name = (By.XPATH, "(//div[2]/div/div[2]/input)[3]")
        self.employee_id = (By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/div[2]/input")
        self.save_button = (By.XPATH, "//button[contains(.,'Save')]")
        self.employee_info_Id = (By.XPATH, "//div[2]/input")
        self.employee_search_button = (By.XPATH, "//button[contains(.,'Search')]")
        self.employee_id_grid = (By.XPATH, "//div[3]/div/div[2]/div/div/div[2]/div")
        self.employee_edit_button = (By.XPATH, "(//div[9]/div/button/i)[1]")
        self.employee_id_profile_value = (By.XPATH, "(//div[2]/div/div/div/div[2]/input)[1]")
        self.delete_employee_button = (By.XPATH, "(//button[2]/i)[1]")
        self.employee_delete_confirmation_message = (By.XPATH, "//p[contains(.,'Are you Sure?')]")
        self.employee_delete_confirmation_yes_option_message = (By.XPATH, "//button[contains(.,' Yes, Delete')]")
        self.save_profile_button = (By.XPATH, "(//button[contains(.,'Save')])[1]")
        self.toast_delete_message = (By.XPATH, "//div[contains(.,'Successfully Deleted')]")
        self.create_login_details_checkbox = (By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div[2]/div/label/span")   
        self.username_input = (By.XPATH, "//div[3]/div/div/div/div[2]/input")  
        self.password = (By.XPATH, "(//div[4]/div/div/div/div[2]/input)[1]")
        self.confirm_password = (By.XPATH, "(//div[4]/div/div/div/div[2]/input)[2]")
        self.search_username = (By.XPATH, "//div[2]/input")

    def goToPimPage(self):
        self.click_abstract(self.pim_sidebarmenu)
        self.validatePimPage()

    def validatePimPage(self):
        self.wait_element_appears(self.pim_title)
    
    def clickAddEmployeeButton(self):
        self.click_abstract(self.add_employee_button)
        self.validateAddEmployeePage()

    def validateAddEmployeePage(self):
        self.wait_element_appears(self.add_employee_title)
        
    def fillAddEmployeeFields(self):       
        self.fillEmployeeInfo()
        #self.click_abstract(self.save_button)	

    def generateEmployeeId(self):
        length = random.randint(10, 12)
        characters = string.ascii_letters + string.digits
        employee_id = ''.join(random.choice(characters) for _ in range(length))
        return employee_id

    def fillEmployeeInfo(self):
        firstName = self.generateRandomFirstName()
        lastName = self.generateRandomLastName()  
        employeeFName = firstName
        employeeLName = lastName
        self.sendkeys_abstract(self.employee_first_name, employeeFName)
        self.sendkeys_abstract(self.employee_last_name, employeeLName) 

    def selectAndFillCreateLoginDetais(self):        
        username = self.generateGenericUsername()
        password = self.generateGenericPassword()
        sleep(10)
        self.click_abstract(self.create_login_details_checkbox)
        self.wait_element_appears(self.username_input)
        self.sendkeys_abstract(self.username_input, username)
        self.sendkeys_abstract(self.password, password)
        self.sendkeys_abstract(self.confirm_password, password)
        self.click_abstract(self.save_button)

    def searchEmployeeByUsername(self):
        self.wait_element_appears(self.search_username)
        employee_username = self.getEmployeeUsername()
        self.sendkeys_abstract(self.search_username, employee_username)

    def generateGenericPassword(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password     
    
    def generateGenericUsername(self):
        first_name_element = self.find_element_abstract(self.employee_first_name)
        first_name = first_name_element.get_attribute("value")
        number = random.randint(100, 999)
        username = f"{first_name.lower()}{number}"
        return username
    
    def getEmployeeUsername(self):
        element = self.find_element_abstract(self.username_input)
        employee_username = element.get_attribute("value")
        return employee_username    

    def addEmployeeWithUsername(self):
        self.clickAddEmployeeButton()
        self.wait_element_appears(self.employee_first_name)
        firstName = self.generateRandomFirstName()
        lastName = self.generateRandomLastName()  
        employeeFName = firstName
        employeeLName = lastName
        self.sendkeys_abstract(self.employee_first_name, employeeFName)
        self.sendkeys_abstract(self.employee_last_name, employeeLName) 
        username = self.generateGenericUsername()
        password = self.generateGenericPassword()
        sleep(10)
        self.click_abstract(self.create_login_details_checkbox)
        self.wait_element_appears(self.username_input)
        self.sendkeys_abstract(self.username_input, username)
        self.sendkeys_abstract(self.password, password)
        self.sendkeys_abstract(self.confirm_password, password)
        self.click_abstract(self.save_button)

    def addEmployee(self):
        self.clickAddEmployeeButton()
        self.fillAddEmployeeFields()
        employee_id = self.getEmployeeId()
        self.click_abstract(self.save_button)
        sleep(10)       
        return employee_id

    def clickSaveButton(self):
        self.click_abstract(self.save_button)

    def getEmployeeId(self):
        element = self.find_element_abstract(self.employee_id)
        self.employee_id_value = element.get_attribute("value")
        return self.employee_id_value        

    def clickEmployeeSearchButton(self):
        self.click_abstract(self.employee_search_button)

    def findEmployeeById(self, employee_id):
        sleep(10)
        self.sendkeys_abstract(self.employee_info_Id, employee_id)
        self.clickEmployeeSearchButton()

    def accessEmployeeProfile(self):
        sleep(10)
        self.openEmployeeProfile()

    def openEmployeeProfile(self):
        self.wait_element_appears(self.employee_id_grid)
        
        self.click_abstract(self.employee_edit_button)
        self.wait_element_appears(self.employee_id_profile_value)

    def validateAndEditEmployeeProfile(self):
        element = self.find_element_abstract(self.employee_id_profile_value)
        profile_id_value = element.get_attribute("value")
        if profile_id_value == self.employee_id_value:
            self.editEmployeeMiddleName()
        else:
            raise AssertionError("ID ({self.employee_id_value}) was not found")

    def editEmployeeMiddleName(self):
        self.sendkeys_abstract(self.employee_middle_name, self.generateRandomMiddleName())
        self.clickSaveProfileButton()
        sleep(10)

    def clickSaveProfileButton(self):   
        self.click_abstract(self.save_profile_button)        
        
    def deleteEmployee(self):
        self.wait_element_appears(self.employee_id_grid)
        self.click_abstract(self.delete_employee_button)
        self.wait_element_appears(self.employee_delete_confirmation_message)
        self.click_abstract(self.employee_delete_confirmation_yes_option_message)

    def validateDeleteToastMessage(self):
        self.wait_element_appears(self.toast_delete_message)

    #self.generate():
    #self.employeeUserName = ("testgenerated" + firstName + lastName).lower()

    def generateRandomFirstName(self):
        return names.get_first_name()
    
    def generateRandomLastName(self):
        return names.get_last_name()
    
    def generateRandomMiddleName(self):
        return names.get_last_name() 
    