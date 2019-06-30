from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        link.click()

    def should_add_item_to_basket(self):
        book_name = self.browser.find_element(By.CSS_SELECTOR, "h1").text
        added_book_name = self.browser.find_element(By.CSS_SELECTOR, ".alert-success strong").text
        assert book_name == added_book_name, "The book name is different"

        price = self.browser.find_element(By.CSS_SELECTOR, "p.price_color").text
        added_price = self.browser.find_element(By.CSS_SELECTOR, ".alert-info strong").text
        assert price == added_price, "The price is different"