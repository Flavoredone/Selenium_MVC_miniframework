#!/usr/bin/env python
# -*- coding: utf8 -*-

from selenium.webdriver.support.ui import Select
from elements.base_element import BaseElement
from utils.locators import *


class DropdownList(BaseElement):
    """BaseElement child class. Implements common logic for <element_name>"""
    def __init__(self, driver, *locator):
        super().__init__(driver)
        self.driver = driver
        self.locator = MainPageLocators
        self.dropdown = self._find_element(*locator)

    def click_dropdown(self):
        self.dropdown.click()

    def select_dropdown_by_value(self, value=1):
        """Works only with <select> dropdowns"""
        select = Select(self.dropdown)
        select.select_by_value(value)

    def select_dropdown_by_text(self, text=''):
        """Works only with <select> dropdowns"""
        select = Select(self.dropdown)
        select.select_by_visible_text(text)

    def select_dropdown_by_locator(self, *locator):
        selected = self._find_element(*locator)
        selected.click()


