from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "a[href$=\"/basket/\"]")

class CartPageLocators(object):
    CART_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")