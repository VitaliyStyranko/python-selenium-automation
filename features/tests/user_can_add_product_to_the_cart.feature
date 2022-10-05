# Created by Vitaliy at 10/2/2022
Feature: User can add product to the cart


  Scenario: User can add product to the cart
    Given Open Amazon page
    When Search for manduka yoga mat
    Then Click on the first product
    And Click on Add to cart button
    Then Open cart page
    And Verify product added to the cart