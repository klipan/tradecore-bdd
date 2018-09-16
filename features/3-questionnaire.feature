Feature: Questionnaire test

    Scenario: Questionnaire page
        When Click Finish button
        Then Required fields are marked in red

    Scenario Outline: Share
        When Select one of "<options>" from Shares
        Then One of the Shares "<options>" is visible

    Examples:
        | options |
        | No |
        | Sometimes |
        | Frequently |

    Scenario Outline: Forex
        When Select one of "<options>" from Forex
        Then One of the Forex "<options>" is visible

    Examples:
        | options |
        | Frequently |
        | No |
        | Sometimes |

    Scenario Outline: Cfds
        When Select one of "<options>" from Cfds
        Then One of the Cfds "<options>" is visible

    Examples:
        | options |
        | Frequently |
        | Sometimes |
        | No |

    Scenario Outline: Spread betting
        When Select one of "<options>" from Spread betting
        Then One of the Spread betting "<options>" is visible

    Examples:
        | options |
        | Sometimes |
        | No |
        | Frequently |

    Scenario Outline: Relevante Experience
        When Select one of "<options>" from Relevante Experience
        Then One of the Relevante Experience "<options>" is visible

    Examples:
        | options |
        | Attended a relevant training course |
        | Had experience of working in the financial sector |
        | No other relevant experience |

    Scenario: Trading platform
        When Select one of "MT5" from Trading platform
        Then One of the Trading platform "MT5" is visible

    Scenario: Currency dropdown is visible
        Then Currency dropdown is displayed

    Scenario Outline: Currency
        When Select one of "<options>" from Currency
        Then One of the Currency "<options>" is visible

    Examples:
        | options |
        | USD |
        | EUR |
        | GBP |

    Scenario Outline: Annual Income
        When Select one of "<options>" from Annual Income
        Then One of the Annual Income "<options>" is visible

    Examples:
        | options |
        | Over $100,000 |
        | $50,000 - $99,999 |
        | $15,000 - $49,999 |
        | Less than $15,000 |

    Scenario Outline: Employment status
        When Select one of "<options>" from Employment status
        Then One of the Employment status "<options>" is visible

    Examples:
        | options |
        | Employed |
        | Self Employed |
        | Retired |
        | Student |
        | Unemployed |

    Scenario Outline: Assets
        When Select one of "<options>" from Assets
        Then One of the Assets "<options>" is visible

    Examples:
        | options |
        | Over $100,000 |
        | $50,000 - $99,999 |
        | $5,000 - $49,999 |
        | Less than $5,000 |

    Scenario: Portal is open
        When Select read terms
        And Click Finish
        Then Test is done
