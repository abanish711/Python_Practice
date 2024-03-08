import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Homepage:

    def SearchBar(self, browser_handle):
        self.browser = browser_handle
        return self.browser.find_element(By.XPATH, "//textarea[@id='APjFqb']")

    def SearchBtn(self, browser_handle):
        self.browser = browser_handle
        return self.browser.find_element(By.NAME, "btnK")

    def News(self,browser_handle):
        self.browser = browser_handle
        return self.browser.find_element(By.LINK_TEXT, "News")
