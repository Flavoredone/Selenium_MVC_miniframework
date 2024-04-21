#!/usr/bin/env python
# -*- coding: utf8 -*-

from forms.main_form import *
from tests.base_test import BaseTest
from utils.test_cases import test_cases


class MainPageTest(BaseTest):
    """Class that implements particular tests"""

    def test_case_1(self):
        """Test case #1 implementation"""
        form = MainForm(self.driver)

        self.assertTrue(form.check_page_loaded())
        self.assertTrue(form.check_here_loaded())
        self.assertTrue(form.click_help_button())
        print("\n" + str(test_cases(1)) + "\n")

    def test_case_2(self):
        """Test case #2 implementation"""
        form = MainForm(self.driver)

        self.assertTrue(form.check_page_loaded())
        self.assertTrue(form.zero_timer_start())
        print("\n" + str(test_cases(2)) + "\n")

    def test_case_3(self):
        """Test case #3 implementation"""
        form = MainForm(self.driver)

        self.assertTrue(form.check_page_loaded())
        self.assertTrue(form.check_here_loaded())
        self.assertTrue(form.form_data_input())
        print("\n" + str(test_cases(3)) + "\n")

    def test_case_4(self):
        """Test case #4 implementation"""
        form = MainForm(self.driver)

        self.assertTrue(form.check_page_loaded())
        self.assertTrue(form.check_here_loaded())
        self.assertFalse(form.form_data_input(password_length=8))
        print("\n" + str(test_cases(4)) + "\n")

    def test_case_5(self):
        """Test case #5 (extra) implementation"""
        form = MainForm(self.driver)

        self.assertTrue(form.check_page_loaded())
        self.assertTrue(form.check_here_loaded())
        self.assertTrue(form.form_data_input())
        self.assertTrue(form.extend_project())
        print("\n" + str(test_cases(5)) + "\n")

