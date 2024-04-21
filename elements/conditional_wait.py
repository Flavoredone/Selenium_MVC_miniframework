#!/usr/bin/env python
# -*- coding: utf8 -*-

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from elements.base_element import BaseElement


class ConditionalWait(BaseElement):
    """Wrapper for WebElement class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_to_be_clickable(self, timeout=10, check_visibility=True, *locator):
        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(*locator))
        except TimeoutException:
            print('Element not clickable!')

        if check_visibility:
            self.wait_until_not_visible()
            self.driver.quit()

        return element

    def is_clickable(self, *locator):
        element = self.wait_to_be_clickable(*locator)
        return element is not None

    def wait_until_not_visible(self, timeout=10, *locator):
        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            print('Element not visible!', 'red')

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self.driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:

                iteration += 1

                visibility = self.driver.execute_script(js, element)
                print('Element {0} visibility: {1}'.format(locator, visibility))

        return element
