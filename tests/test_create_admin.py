import pytest
from pages.home_page import HomePage
from pages.user_management_page import UserManagement
from pages.add_user_menu_page import AddUser
#To run: python -v pytest 
#To run: pytest -v .\tests\test_create_admin.py

@pytest.mark.usefixtures('setup_teardown')
class TestCreateAnAdmin:
    def test_create_an_admin(self):
        home_page = HomePage()
        user_management_page = UserManagement()
        add_user_page = AddUser()
        employee_username = add_user_page.addEmployeeFullSteps()
        home_page.goToAdminPage()
        user_management_page.validate_um_page()
        user_management_page.searchUserByUserName(employee_username)
        user_management_page.editAdminUser()        
        home_page.goToAdminPage()
        user_management_page.validate_um_page()
        user_management_page.searchUserByUserName(employee_username)
        user_management_page.deleteUser()
