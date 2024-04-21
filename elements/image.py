#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import time
import pyautogui
from elements.base_element import BaseElement
from utils.locators import MainPageLocators


def get_download_path():
    """Returns the default downloads path for windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


class Image(BaseElement):
    """BaseElement child class. Implements common logic for <element_name>"""
    def __init__(self, driver, *locator):
        super().__init__(driver)
        self.image = self._find_element(*locator)
        self.locator = MainPageLocators

    def click_image(self):
        if self.image:
            self.image.click()

    def send_image(self):
        if self.image:
            self.image.click()
            time.sleep(1)
            pyautogui.write(get_download_path() + r'\avatar.png')
            pyautogui.press('enter')
        else:
            msg = ' with locator {0} not found'
            raise AttributeError(msg.format(self.locator))
