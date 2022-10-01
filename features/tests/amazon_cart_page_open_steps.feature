# Created by Vitaliy at 9/29/2022
Feature: Test user can open Amazon Cart page


  Scenario: User can open Amazon Cart
    Given Open amazon page
    When Click on Cart icon
    Then Verifies Your Amazon Cart is empty visible
