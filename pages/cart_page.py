from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), \
        "There are items in the basket, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), \
        "There is no empty basket message, but should be"