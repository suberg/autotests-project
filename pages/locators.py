from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "a[href$=\"/basket/\"]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    CART_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD_REPEAT_INPUT = (
        By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators(object):
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "h1")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDED_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
