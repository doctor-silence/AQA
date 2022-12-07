import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.Full_Name).send_keys('vdsv')
        self.element_is_visible(self.locators.Email).send_keys('vdsv@dv.ru')
        self.element_is_visible(self.locators.Current_Address).send_keys('vdsv')
        self.element_is_visible(self.locators.Permanent_Address).send_keys('vdsv')
        self.element_is_visible(self.locators.Submit).click()


    def check_filled_form(self):



