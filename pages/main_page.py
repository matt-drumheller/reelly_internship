from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN_BUTTON = (By.CSS_SELECTOR, '.menu-twobutton')

    def open_main(self):
        self.open_url('https://soft.reelly.io/')


