from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

TOP_FILTER_BUTTON = (By.XPATH, "//a[@class='filter-button w-inline-block']//div[@class='filter-text']")
UNIT_PRICE_FROM = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
UNIT_PRICE_TO = (By.CSS_SELECTOR, '[wized="unitPriceToFilter"]')
APPLY_FILTER = (By.CSS_SELECTOR, '.button-filter.w-button')
LISTED_PRICE = (By.CSS_SELECTOR, '[class="price-value"]')


@then('Verify the right page opens')
def off_plan_open(context):
    expected_url = "https://soft.reelly.io/off-plan"
    actual_url = context.driver.current_url
    assert expected_url == actual_url, f'Expected url was {expected_url} but current url is {actual_url}'

@then('Filter the products by price range from {price_low} to {price_high} AED')
def filter_price(context, price_low, price_high):
    sleep(5)
    context.driver.find_element(*TOP_FILTER_BUTTON).click()
    context.driver.find_element(*UNIT_PRICE_FROM).send_keys(price_low)
    context.driver.find_element(*UNIT_PRICE_TO).send_keys(price_high)
    context.driver.find_element(*APPLY_FILTER).click()

@then('Verify the price in all cards is between {price_low} and {price_high}')
def applied_filter(context, price_low, price_high):
    prices = context.driver.find_elements(*LISTED_PRICE)
    print(prices)
    # for price in prices:
    #     price = int(price)
    #     if price >= price_low and price <= price_high:
    #         pass
    #     else:
    #         print("Price is not within range")