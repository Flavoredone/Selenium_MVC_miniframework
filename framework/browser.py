#!/usr/bin/env python
# -*- coding: utf8 -*-

from framework.settings_data_manager import DataManager


class Browser(object):
    """Class solves problem implementation logic for different driver types"""

    @staticmethod
    def goToUrl(driver):
        return driver.get(DataManager().set_url())

    @staticmethod
    def closeBrowser(driver):
        return driver.close()
