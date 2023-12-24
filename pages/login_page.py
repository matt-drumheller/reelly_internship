from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class LoginPage(Page):
    LOG_IN_BUTTON = (By.CSS_SELECTOR, '[class*="login-button"]')

    def log_in(self):
        self.