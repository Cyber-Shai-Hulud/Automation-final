from .pages.product_page import PageObject
import time


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_in_basket_the_same_as_on_page()
    page.product_price_same_as_in_basket()
