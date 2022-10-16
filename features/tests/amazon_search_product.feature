# Created by Vitaliy at 10/16/2022
Feature: Test for amazon search product

  Scenario: Verify that product on Amazon has name and image
    Given open Amazon page
    When Search for white sage
    Then Verify that every product has a name and an image