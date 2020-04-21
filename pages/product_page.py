from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Basket button is not presented"

    def should_be_equal_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME)
        assert product_name == basket_name, "Basket product name is not equal product name!"

    def should_be_equal_cost(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE)
        assert product_price == basket_price, "Basket price is not equal product price!"
