import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from utilities.globalVars import globalVars
import pdb
#To run: python -v pytest 
#To run: pytest -v .\tests\test_create_edit_del_employee.py


@pytest.mark.usefixtures('setup_teardown')
class TestCreateEditDeleteAnEmployee:
    def test_create_edit_del_employee(self):
        login_page = LoginPage()
        home_page = HomePage()
        pim_page = PimPage()
        login_page.wait_elements_load()
        login_page.perform_login(globalVars.userName, globalVars.userPassword)
        home_page.validate_successful_login()
        pim_page.goToPimPage()
        employee_id = pim_page.addEmployee()
        #pim_page.fillAddEmployeeFields()
        #pim_page.getEmployeeId()
        #pim_page.clickSaveButton()
        pim_page.goToPimPage()
        pim_page.findEmployeeById(employee_id)
        pim_page.accessEmployeeProfile()
        pim_page.editEmployeeMiddleName()
        pim_page.goToPimPage()
        pim_page.findEmployeeById(employee_id)
        pim_page.deleteEmployee()
        pim_page.validateDeleteToastMessage()
   