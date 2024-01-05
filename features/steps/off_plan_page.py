from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify the right page opens')
def off_plan_open(context):
    context.app.off_plan_page.verify_page_opens()


@then('Filter the products by price range from {price_low} to {price_high}')
def filter_price(context, price_low, price_high):
    context.app.off_plan_page.filter_pricing(price_low, price_high)


@then('Verify the price in all cards is between {price_low} and {price_high}')
def applied_filter(context, price_low, price_high):
    context.app.off_plan_page.filter_verification(price_low, price_high)
    # for price in prices:
    #     price = int(price)
    #     if price >= price_low and price <= price_high:
    #         pass
    #     else:
    #         print("Price is not within range")
