#!/usr/bin/env python
# -*- coding: utf8 -*-

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    HERE = (By.CLASS_NAME, 'start__link')
    HELP = (By.CLASS_NAME, 'help-form__help-button')
    WAIT = (By.CLASS_NAME, 'help-form__response')
    TIMER = (By.CLASS_NAME, 'timer')

    PASSWORD = (By.XPATH, "//input[@placeholder='Choose Password']")
    MAIL = (By.XPATH, "//input[@placeholder='Your email']")
    DOMAIN = (By.XPATH, "//input[@placeholder='Domain']")

    CHECKBOX = (By.CLASS_NAME, 'checkbox__box')
    DROPDOWN = (By.CLASS_NAME, 'dropdown__field')
    DROPDOWN_ITEM_2 = (By.XPATH, "//div[text()='.org']")

    NEXT = (By.CLASS_NAME, 'button--secondary')

    AVATAR = (By.XPATH, "//h2[text()='This is me']")
    DOWNLOAD_IMAGE = (By.XPATH, "//button[text()='Download image']")
    UPLOAD_IMAGE = (By.XPATH, "//a[@class='avatar-and-interests__upload-button']")

    CHECKBOX_LABEL_UNSELECT = (By.XPATH, "//label[@for='interest_unselectall']")
    CHECKBOX_LABEL_PONIES = (By.XPATH,  "//label[@for='interest_ponies']")
    CHECKBOX_LABEL_POLO = (By.XPATH,  "//label[@for='interest_polo']")
    CHECKBOX_LABEL_DOUGH = (By.XPATH, "//label[@for='interest_dough']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")

    DETAILS = (By.XPATH, "//h3[text()='Personal details']")

