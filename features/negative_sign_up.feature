Feature: Tradecore app failed

    Scenario: Sign up
        Given Go to Tradecore site
        When Click Next
        Then Required fields become red


    Scenario Outline: Wrong email
        When Enter "<email>"
        Then Email field throws an error

    Examples:

        | email |
        | test |
        | test@ |
        | test@54.c |
        | test32@5454.a |

    Scenario Outline: Wrong password
        When Type "<password>"
        Then Password field throws an error

    Examples:
        | password |
        | test |
        | TeT3 |
        | 12432432:" |

    Scenario Outline: Phone number
        When Enter "<phone>" number
        Then Phone number field throws an error
    Examples:
        | phone |
        | +3 |
        | +2329871837821354563254 |
        | +testtest |

    Scenario: Unknown flag in phone field
        When Enter "3" to phone number field
        Then Flag does not show up

    Scenario: Cuban flag in phone field
        When Enter Cuban dial code in phone field
        Then Cuban flag shows up

    Scenario: Leave empty Date of birth field
        When Leave date of birth field empty
        Then Error message is showing

    Scenario: Date of birth field
        When Enter "09/09/2000" in date of birth field
        Then Phone field return an error message

