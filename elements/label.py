#!/usr/bin/env python
# -*- coding: utf8 -*-

from elements.base_element import BaseElement
from utils.locators import *


class Label(BaseElement):
    """BaseElement child class. Implements common logic for <element_name>"""
    def __init__(self, driver, *locator):
        super().__init__(driver)
        self.locator = MainPageLocators
        self.label = self._find_element(*locator)

    def click_label(self):
        if self.label:
            self.label.click()

    def get_attribute(self, attr_name, **kwargs):
        if self.label:
            return self.label.get_attribute(attr_name)
