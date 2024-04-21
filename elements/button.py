#!/usr/bin/env python
# -*- coding: utf8 -*-

from elements.base_element import BaseElement
from utils.locators import *


class Button(BaseElement):
    """BaseElement child class. Implements common logic for <element_name>"""

    def __init__(self, driver, *locator):
        super().__init__(driver)
        self.locator = MainPageLocators
        self.button = self._find_element(*locator)

    def click_button(self):
        """Clicks button"""
        if self.button:
            self.button.click()

    def get_text(self):
        """Gets button text"""
        elements = self._find_element()
        result = []

        for element in elements:
            text = ''

            try:
                text = str(element.text)
            except Exception as e:
                print('Error: {0}'.format(e))

            result.append(text)

        return result
