# Created by Vitaliy at 9/28/2022
Feature: Test for amazon Sign in page opened when clicking Order


  Scenario: User can open Sign in page by clicking Order
    Given Open amazon main page
    When Click on Return & Order button
    Then Verify Sign in header is visible
    Then Verify email input field is present
	
