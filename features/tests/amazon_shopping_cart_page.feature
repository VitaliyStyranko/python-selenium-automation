# Created by Vitaliy at 11/7/2022
Feature: Shopping cart test case

  Scenario:'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present
