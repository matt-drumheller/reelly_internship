Feature: Filtering by unit price test - Scenario 19

  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    When Log in to the page
    And Click on "off plan" at the left side of menu
    Then Verify the right page opens
    And Filter the products by price range from '1200000' to '2000000' AED
    And Verify the price in all cards is between '1200000' and '2000000'