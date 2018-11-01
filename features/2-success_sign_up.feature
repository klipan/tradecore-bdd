Feature: Success sign up

  Scenario: Verify color of Next button
    Then Color of Next button is green

  Scenario: Fill out all required fields
    When Enter all required fields
    Then User is redirected to a questionnaire
