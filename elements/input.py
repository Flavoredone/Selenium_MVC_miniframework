#!/usr/bin/env python
# -*- coding: utf8 -*-

from elements.base_element import BaseElement
from utils.locators import *


class Input(BaseElement):
    """BaseElement child class. Implements common logic for <element_name>"""
    def __init__(self, driver, *locator):
        super().__init__(driver)
        self.locator = MainPageLocators
        self.input = self._find_element(*locator)

    def click_input(self):
        if self.input:
            self.input.click()

    def clear_input(self):
        if self.input:
            self.input.clear()

    def send_keys(self, keys):
        keys = keys.replace('\n', '\ue007')
        if self.input:
            self.click_input()
            self.clear_input()
            self.input.send_keys(keys)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self.locator))