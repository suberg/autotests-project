import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .pages.main_page import MainPage

class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        email = str(time.time()) + "@fakemail.org"
        password = 'vw2CxUbNviGWpbxokgs8'
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_basket()
        page.should_add_item_to_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_add_item_to_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_basket_message()
    cart_page.should_not_be_basket_items()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
