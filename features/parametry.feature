Feature: Step Params
  Scenario: Blenders
    Given I put "apples" in a blender
    When I switch the blender on
    Then it should transform into "apple juice"