Feature: Step Params
  Scenario Outline: Blenders
    Given I put "<thing>" in a blender
    When I switch the blender on
    Then it should transform into "<other_thing>"

    Examples:
    | thing       | other_thing |
    | apples      | apple juice |
    | iPhone      | toxic waste |