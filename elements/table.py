#!/usr/bin/env python
# -*- coding: utf8 -*-

from elements.base_element import BaseElement
from utils.locators import *


class Table(BaseElement):
    """BaseElement child class. Implements common logic for <element_name>"""
    def __init__(self, driver, *locator):
        super().__init__(driver)
        self.locator = MainPageLocators
        self.table = self._find_element(*locator)

    def click_table(self):
        if self.table:
            self.table.click()
