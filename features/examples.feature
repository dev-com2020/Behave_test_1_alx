Feature: Step Params
  Scenario Outline: Blenders
    Given I put "<things>" in a blenders
    When I switch the blender on!
    Then it should transform into "<other_things>!"

    Examples:
    | things       | other_things |
    | apples       | apple juice  |
    | iphone       | toxic waste  |