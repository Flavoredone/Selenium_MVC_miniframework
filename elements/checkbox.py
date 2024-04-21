#!/usr/bin/env python
# -*- coding: utf8 -*-

from elements.base_element import BaseElement
from utils.locators import *


class CheckBox(BaseElement):
    """BaseElement child class. Implements common logic for <element_name>"""
    def __init__(self, driver, *locator):
        super().__init__(driver)
        self.locator = MainPageLocators
        self.checkbox = self._find_element(*locator)

    def click_checkbox(self):
        if self.checkbox:
            self.checkbox.click()
