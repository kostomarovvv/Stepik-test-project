from cgitb import text
from itertools import tee
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON) 
        add_button.click()
        self.solve_quiz_and_get_code()
        productName = self.get_product_name()
        self.test_product_name(productName)
        productPrice = self.get_product_price()
        self.test_product_price(productPrice)

    def test_product_name(self, productName):
        messageElement = self.browser.find_element(*ProductPageLocators.MESSAGE_ELEMENT)
        print(f'Message Name: {messageElement.text}')
        print(f'Product Name: {productName}')
        assert messageElement.text==productName, "Name of product is incorrect"

    def test_product_price(self, productPrice):
        busketElement = self.browser.find_element(*ProductPageLocators.BUSKET_ELEMENT)
        print(f'Product price: {productPrice}')
        print(f'Busket  price: {busketElement.text}')
        assert productPrice==busketElement.text, "Price in the busket is incorrect"

    def get_product_name(self):
        productElement = self.browser.find_element(*ProductPageLocators.PRODUCT_ELEMENT)
        return productElement.text

    def get_product_price(self):
        priceElement = self.browser.find_element(*ProductPageLocators.PRICE_ELEMENT)
        return priceElement.text        