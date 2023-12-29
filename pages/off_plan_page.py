from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class OffPlanPage(Page):
    TOP_FILTER_BUTTON = (By.XPATH, "//a[@class='filter-button w-inline-block']//div[@class='filter-text']")
    UNIT_PRICE_FROM = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
    UNIT_PRICE_TO = (By.CSS_SELECTOR, '[wized="unitPriceToFilter"]')
    APPLY_FILTER = (By.CSS_SELECTOR, '.button-filter.w-button')
    LISTED_PRICE = (By.CSS_SELECTOR, '[class="price-value"]')

    def verify_page_opens(self):
        expected_url = "https://soft.reelly.io/off-plan"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected url: {expected_url}, Actual url: {actual_url}'

    def filter_pricing(self, price_low, price_high):
        sleep(5)
        self.click(*self.TOP_FILTER_BUTTON)
        self.input({price_low}, *self.UNIT_PRICE_FROM)
        self.input({price_high}, *self.UNIT_PRICE_TO)
        self.click(*self.APPLY_FILTER)

    def filter_verification(self, price_low, price_high):
        price = self.find_element(*self.LISTED_PRICE).text
        assert price_low <= price <= price_high, f'Not in range'


