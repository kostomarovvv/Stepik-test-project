from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-primary")   
    MESSAGE_ELEMENT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner > strong")    
    PRODUCT_ELEMENT = (By.CSS_SELECTOR, ".col-sm-6 h1")    
    PRICE_ELEMENT = (By.CSS_SELECTOR, ".col-sm-6 .price_color")    
    BASKET_ELEMENT = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > .alertinner p strong")    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class BasketPageLocators():
    BASKET_LIST = (By.CSS_SELECTOR, "#content_inner form")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")