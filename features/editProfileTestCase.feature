Feature: Edit user profile on James app

  Scenario: Change user First Name
    Given James app is running with user already logged in
    Then I tap on main menu button
    When I tap on the tile with users names
    Then I am taken to the Profile screen
    And I change users first name to "WhatsUp"
    Then I tap Done button
    Then Success toast message is displayed
    And Account screen shows new name "WhatsUp" on user profile tile