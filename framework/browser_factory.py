#!/usr/bin/env python
# -*- coding: utf8 -*-

from selenium import webdriver

from framework.browser import Browser
from framework.settings_data_manager import DataManager
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions


class BrowserFactory(Browser):
    """Class solves problem implementation logic for different driver types"""

    def __init__(self):
        self.driver = webdriver

    def getBrowser(self):
        c_options = COptions()
        f_options = FOptions()
        settings = DataManager()
        browser_name = settings.set_settings()['browser']

        if browser_name == 'Firefox':
            for setting in settings.set_settings()['f'].values():
                f_options.add_argument(str(setting))
            return self.driver.Firefox(options=f_options)

        elif browser_name == 'Chrome':
            for setting in settings.set_settings()['c'].values():
                c_options.add_argument(str(setting))
            return self.driver.Chrome(options=c_options)

        raise Exception("No such " + str(browser_name) + " browser exists")


class DriverSingleton(object):
    """Class provides single access point to get actual driver instance"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
