from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def should_add_item_to_basket(self):
        book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text
        added_book_name = self.browser.find_element(
            *ProductPageLocators.ADDED_BOOK_NAME).text
        assert book_name == added_book_name, "The book name is different"

        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        added_price = self.browser.find_element(
            *ProductPageLocators.ADDED_PRICE).text
        assert price == added_price, "The price is different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
