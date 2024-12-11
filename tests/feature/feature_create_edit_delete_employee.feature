Feature: Create, Edit, and Delete an Employee

  Scenario: Create an Employee
    Given I am an admin user with permissions to add a new employee
    When I click on Create Employee
    And I fill in the "Name" and "Last Name" fields
    And I click on the Save button
    Then I should see the validation message "Employee created successfully"

  Scenario: Edit an Employee
    Given I am an admin user with permissions to edit the employee
    When I find the employee by ID
    And I click on his ID in the results grid
    And I access the Employee Profile page
    And I change the Middle Name
    And I click on the Save button
    Then I should see the validation message "Employee updated successfully"

  Scenario: Delete an Employee
    Given I am an admin user with permissions to delete the employee
    When I find the employee by ID
    And I click on the trash bin icon related to the User ID in the results grid
    And I should see the confirmation message "Are you sure you want to delete this employee?"
    And I click on the confirm button
    Then I should see the validation message "Employee deleted successfully"