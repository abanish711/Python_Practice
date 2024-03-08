import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    browser_handle = webdriver.Chrome()
    browser_handle.implicitly_wait(2)
    browser_handle.get("https://www.google.co.uk")
    browser_handle.maximize_window()
    return browser_handle



