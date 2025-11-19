Feature: Automation Practice interactions
  As an automation engineer
  I want to exercise key controls on the Automation Practice page

  Background:
    Given I open the practice page

  @smoke
  Scenario: Verify title and interact with checkbox and radio
    Then I select the checkbox
    And I select the radio option

  @regression
  Scenario Outline: Select dropdown and suggestions (data-driven)
    When I select dropdown value "<dropdown>"
    And I type suggestion "<suggestion>"
    And I select second suggestion from the list
    Then the selected dropdown should be "<dropdown>"

    Examples:
      | dropdown | suggestion |
      | Option1  | Ind       |
      | Option2  | Australi  |
