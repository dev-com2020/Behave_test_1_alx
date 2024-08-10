Feature: Wyszukiwanie produktu
  Scenario: Wyszukujemy Plaid Cotton Shirt
    Given wchodzimy na strone madison island
    When uzytkownik wpisuje w pole wyszukiwania "Plaid Cotton Shirt"
    And klika w przycisk szukaj
    And robie screenshot
    Then strona zawiera tresc "Plaid Cotton Shirt"