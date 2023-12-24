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
    context.driver.get('https://soft.reelly.io/')
    sleep(7)
    #sleep put in to wait for auto-sign in page to load


@when('Log in to the page')
def log_in(context):
    context.driver.find_element(By.ID, "email-2").send_keys('matthew.drumheller@gmail.com')
    context.driver.find_element(By.ID, "field").send_keys('Goldteam138')
    context.driver.wait.until(EC.element_to_be_clickable(LOG_IN_BUTTON))
    context.driver.find_element(*LOG_IN_BUTTON).click()

@when('Click on "off plan" at the left side of menu')
def off_plan_page(context):
    context.driver.find_element(*OFF_PLAN_BUTTON).click()



