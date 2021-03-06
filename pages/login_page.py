import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Incorrect URL!"

    def should_be_login_form(self):
        # проверка, что есть форма логина на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented!"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации есть на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Register form is not presented!"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        pass_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        pass_confirm_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        email_field.send_keys(email)
        pass_field.send_keys(password)
        pass_confirm_field.send_keys(password)
        time.sleep(1)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
