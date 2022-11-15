# Created by Vitaliy at 11/08/2022
Feature: User can select and search in a department test case

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by value hpc
    Then Search for haritaki
    And Click on search btn
    And Verify hpc department is selected

  Scenario: User can see the New Arrivals deals in the Clothing department
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals options
    Then Verify New Arrivals options present

