#!/usr/bin/env python
# -*- coding: utf8 -*-

from termcolor import colored
from elements.image import Image
from forms.base_form import BaseForm
from elements.checkbox import CheckBox
from elements.dropdown_list import DropdownList
from elements.label import Label
from elements.input import Input
from elements.button import Button
from utils.locators import *
from utils.random_util import *


class MainForm(BaseForm):
    """BaseForm child class. Implements common logic for MainPageTest module"""
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        """Method checks that main page is open"""
        label_here = Label(self.driver, *self.locator.HERE)

        if label_here:
            print(colored('Step 1 - Main page is open', 'green'))
            return True
        return False

    def check_here_loaded(self):
        """Method checks that "game page" is open and clicks help button"""
        label_here = Label(self.driver, *self.locator.HERE)
        label_here.click_label()

        help_button = Button(self.driver, *self.locator.HELP)
        help_button.click_button()

        if help_button:
            print(colored('Step 2 - Game page is open', 'green'))
            return True
        return False

    def click_help_button(self):
        """Method checks that "game page" is open and help response is displayed"""
        here_button = Button(self.driver, *self.locator.HELP)
        here_button.click_button()

        label_wait = Label(self.driver, *self.locator.WAIT)
        if label_wait:
            print(colored('Step 3 - Help response is displayed', 'green'))
            return True
        return False

    def zero_timer_start(self):
        """Method checks that "game page" is open and the timer starts from zero"""
        here_button = Button(self.driver, *self.locator.HERE)
        here_button.click_button()

        timer = Label(self.driver, *self.locator.TIMER)
        if timer.get_attribute('textContent') == '00:00:00':
            print(colored('Step 2 - Game page is open; The timer starts from zero', 'green'))
            return True
        return False

    def form_data_input(self, password_length=10):
        """
        Method inputs random email, password, domain,
        accepts terms and conditions and clicks "Next"
        button to navigate to the next card
        """
        util = RandomUtil()

        password_input = Input(self.driver, *self.locator.PASSWORD)
        mail_input = Input(self.driver, *self.locator.MAIL)
        domain_input = Input(self.driver, *self.locator.DOMAIN)
        checkbox_terms = CheckBox(self.driver, *self.locator.CHECKBOX)
        dropdown = DropdownList(self.driver, *self.locator.DROPDOWN)
        next_button = Button(self.driver, *self.locator.NEXT)

        password_input.send_keys(util.generate_password(password_length))
        mail_input.send_keys(util.generate_mail())
        domain_input.send_keys(util.generate_domain())

        checkbox_terms.click_checkbox()
        dropdown.click_dropdown()
        dropdown.select_dropdown_by_locator(*self.locator.DROPDOWN_ITEM_2)
        next_button.click_button()

        try:
            avatar_label = Label(self.driver, *self.locator.AVATAR)
            if avatar_label:
                print("Step 3 - The second card is open")
                return True
        except Exception:
            print("Step 3 - The second card isn't open")
            return False

    def extend_project(self):
        """
        Method continues to fill the form (loads avatar image, selects RadioButtons, etc.
        Note: compatible with windows only (downloaded image file path), uses time.sleep
        (to fill path in explorer), sorry, couldn't find a better solution, send_keys() method
        do not work in this case(
        """
        checkbox_unselect = CheckBox(self.driver, *self.locator.CHECKBOX_LABEL_UNSELECT)
        checkbox_dough = CheckBox(self.driver, *self.locator.CHECKBOX_LABEL_DOUGH)
        checkbox_polo = CheckBox(self.driver, *self.locator.CHECKBOX_LABEL_POLO)
        checkbox_ponies = CheckBox(self.driver, *self.locator.CHECKBOX_LABEL_PONIES)
        next_button = Button(self.driver, *self.locator.NEXT_BUTTON)
        download_image = Image(self.driver, *self.locator.DOWNLOAD_IMAGE)
        upload_image = Image(self.driver, *self.locator.UPLOAD_IMAGE)

        checkbox_unselect.click_checkbox()
        checkbox_dough.click_checkbox()
        checkbox_polo.click_checkbox()
        checkbox_ponies.click_checkbox()
        download_image.click_image()
        upload_image.send_image()
        self.driver.implicitly_wait(2)
        next_button.click_button()
        try:
            details_label = Label(self.driver, *self.locator.DETAILS)
            if details_label:
                print(colored('Next page opened', 'green'))
                return True
        except Exception:
            print(colored('There may be a problem loading the image, please try running the test again', 'green'))
            return False
