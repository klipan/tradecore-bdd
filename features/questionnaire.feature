Feature: Questionnaire test

    Scenario Outline: Shares
    When Select one of "<answers>" from Shares
    Then One of the Shares dropdown "<answers>" will be visible

    Examples:
      | answers    |
      | Frequently |
      | Sometimes  |
      | No         |
