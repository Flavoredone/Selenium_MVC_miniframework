#!/usr/bin/env python
# -*- coding: utf8 -*-

import json


class DataManager(object):
    """Class that reads/writes data to set up project/tests"""

    @staticmethod
    def set_settings():
        with open('../framework/settings.json', 'r') as file:
            settings = json.load(file)
        return settings

    @staticmethod
    def set_url():
        with open('../framework/data.json', 'r') as file:
            url = json.load(file).get('url')
        return url

    @staticmethod
    def generate_settings():
        with open('../framework/settings.json', 'a') as f:
            f.write(json.dumps({
                "browser": "Chrome",
                'c': {"chrome_1": "--no-sandbox",
                      "chrome_2": "disable-infobars",
                      "chrome_3": "--disable-extensions",
                      "chrome_4": "--start-fullscreen",
                      "chrome_5": "--disable-gpu",
                      },
                'f': {"firefox_1": "--headless",
                      "firefox_2": "--start-fullscreen",
                      "firefox_3": "--disable-gpu",
                      }
            }, ensure_ascii=False, indent=3))

    @staticmethod
    def generate_url():
        with open('../framework/data.json', 'a') as f:
            f.write(json.dumps({"url": "https://userinyerface.com/"}, ensure_ascii=False, indent=3))

