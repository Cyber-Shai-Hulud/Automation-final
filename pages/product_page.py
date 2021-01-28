from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math


class PageObject(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def product_name_in_basket_the_same_as_on_page(self):
        added_to_basket_name_product = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME).text
        product_name_on_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert added_to_basket_name_product == product_name_on_page, 'Wrong name displayed in basket'

    def product_price_same_as_in_basket(self):
        added_to_basket_product_price = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_PRICE).text
        book_price_product_page = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert added_to_basket_product_price == book_price_product_page, 'Wrong price displayed in basket'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
