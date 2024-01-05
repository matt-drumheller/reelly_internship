from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(7)
    # sleep put in to wait for auto-sign in page to load


@when('Log in to the page')
def log_in(context):
    context.app.login_page.log_in()


@when('Click on "off plan" at the left side of menu')
def off_plan_page(context):
    context.app.main_page.off_plan_button()
