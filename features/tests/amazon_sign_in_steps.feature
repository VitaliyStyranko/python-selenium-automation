# Created by Vitaliy at 11/3/2022
Feature: Sign in test cases

  Scenario:Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened