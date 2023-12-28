from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class LoginPage(Page):
    LOG_IN_BUTTON = (By.CSS_SELECTOR, '[class*="login-button"]')
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")

    def log_in(self):
        self.input('matthew.drumheller@gmail.com', *self.EMAIL_FIELD)
        self.input('Goldteam138',*self.PASSWORD_FIELD)
        self.click(*self.LOG_IN_BUTTON)
