#!/usr/bin/env python
# -*- coding: utf8 -*-

from framework.settings_data_manager import DataManager
from elements.base_element import BaseElement
from selenium.common.exceptions import TimeoutException


class BaseForm(BaseElement):
    """Parent class for each form and page"""
    def __init__(self, driver, base_url=DataManager.set_url()) -> None:
        super().__init__(driver, base_url)
        self.base_url = base_url
        self.driver = driver
        self.timeout = 10

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get(self, url):
        self.driver.get(url)
        self.driver.wait_page_loaded()

    def go_back(self):
        self.driver.back()
        self.driver.wait_page_loaded()

    def refresh(self):
        self.driver.driver.refresh()
        self.driver.wait_page_loaded()

    def screenshot(self, file_name='../utils/screenshot.png'):
        self.driver.save_screenshot(file_name)

    def scroll_down(self, offset=0):
        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        if offset:
            self.driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        self.driver.switch_to.default_content()

    def get_page_source(self):
        source = ''
        try:
            source = self.driver.page_source
        except TimeoutException:
            print('Can not get page source')

        return source

    def check_js_errors(self, ignore_list=None):
        ignore_list = ignore_list or []

        logs = self.driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)
