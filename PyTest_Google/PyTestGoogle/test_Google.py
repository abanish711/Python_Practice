import time

import pytest
from selenium.webdriver.common.by import By

from PyTestGoogle import PageObjects


def test_google1(setup):
    print("Initiating Google for test_google1\nSearching for UK by entering Britain")
    browser_handle = setup
    home = PageObjects.Homepage()
    home.SearchBar(browser_handle).send_keys("Britain")
    home.SearchBtn(browser_handle).click()
    home.News(browser_handle).click()
    time.sleep(2)
    browser_handle.close()

#EXAMPLE _ WHEN SINGLE TEST USING THE FIXTURE SETUP
