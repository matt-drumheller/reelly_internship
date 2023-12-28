from pages.base_page import Page
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.off_plan_page import OffPlanPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.off_plan_page = OffPlanPage(driver)