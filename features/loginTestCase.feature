Feature: Login Feature

  Scenario: Failed login by entering wrong code
    Given James app is running
    When I enter a fake phone number "3022065094"
    And I tap "Continue" button on phone screen
    Then I enter the invalid pin "111111"
    When I tap "Continue" on pin validation screen
    Then Login fails due to invalid credentials

  Scenario: User logs into James successfully
    Given James app is open and running
    When I enter my phone number "3022065094"
    And I tap "Continue" on enter phone screen
    Then I get the verification code from an SMS
    And I enter the "code" on code screen
    When I tap "Continue" on code screen
    Then I am logged into James app
