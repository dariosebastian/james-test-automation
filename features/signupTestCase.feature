Feature: Create Account functionality

  Scenario: Successful create account via SMS verification
    Given James app is launched and running
    When I enter the phone number "New phone"
    And I tap "Continue" on phone number screen
    Then I get the verification code from the SMS received
    And I enter the "code" on code validation screen
    When I tap "Continue" on code validation screen
    Then I enter my email address "dario@test2.com"
    And I tap continue on email address screen
    Then I enter my first name and last name
    And I tap continue on enter name screen
    Then I am successfully logged in

