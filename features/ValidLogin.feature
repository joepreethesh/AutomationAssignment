Feature: Validating Login functionality for Standard_User and Performance_Glitch_User
  Scenario Outline:
    Given web page is launched
    Then User enters valid credentials "<user>"
    Then login screen should be displayed
    When clciked on Hamburger menu icon
    Then Logout option should be displayed
    When clicked on LogOut button
    Then Login screen is displayed
    Examples:
    |user|
    |standard_user|





