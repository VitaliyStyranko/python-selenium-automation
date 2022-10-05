# Created by Vitaliy at 10/4/2022
Feature: Test for user can open Amazon Best Seller page


  Scenario: User can open Amazon Best Seller page by clicking Best Sellers button
    Given Open amazon main page
    When Click on Best Sellers button
    Then Verify header has 5 links