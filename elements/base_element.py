#!/usr/bin/env python
# -*- coding: utf8 -*-

from framework.settings_data_manager import DataManager
from selenium.webdriver.common.action_chains import ActionChains


class BaseElement(object):
    """Wrapper for WebElement class"""
    def __init__(self, driver, base_url=DataManager.set_url()):
        self.base_url = base_url
        self.driver = driver

    def _find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def hover(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    @staticmethod
    def is_presented(element):
        return element is not None

    @staticmethod
    def is_visible(element):
        if element:
            return element.is_displayed()

        return False

    def get_text(self, *locator):
        element = self._find_element(*locator)
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_attribute(self, attr_name, *locator):
        element = self._find_element(*locator)
        if element:
            return element.get_attribute(attr_name)
