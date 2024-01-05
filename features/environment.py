from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
###GOOGLE CHROME###
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

###HEADLESS MODE - GOOGLE CHROME###
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

###FIREFOX###
    # service = Service(executable_path= r"C:\Users\matth\OneDrive\Desktop\reelly_internship\geckodriver")
    # context.driver = webdriver.Firefox(service=service)


### BROWSERSTACK ###
    # bs_user = 'matthewdrumhelle_OWG1Fs'
    # bs_key = 'euKxrcix4gThpk95ZhAF'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Big Sur',
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    driver_wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()