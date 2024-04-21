#!/usr/bin/env python
# -*- coding: utf8 -*-


import unittest
import warnings

from framework.browser import Browser
from framework.browser_factory import BrowserFactory


class BaseTest(unittest.TestCase, Browser):
    """Class that implements common pre- and post-conditions for each test"""

    def setUp(self) -> None:
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver = BrowserFactory().getBrowser()
        Browser().goToUrl(self.driver)

    def tearDown(self):
        Browser().closeBrowser(self.driver)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
