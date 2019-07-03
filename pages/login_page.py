from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Current URL does not contain the /login part. Maybe you are not on the login page?"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-email")
        email_field.send_keys(email)

        password_field = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-password1")
        password_field.send_keys(password)

        password_repeat_field = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-password2")
        password_repeat_field.send_keys(password)
        button = self.browser.find_element(By.NAME, "registration_submit")
        button.click()
