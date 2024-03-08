import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser_driver:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(3)


class Homepage:

    def __init__(self, driver_obj):
        self.page_driver = driver_obj

    def downloadBtn(self):
        return self.page_driver.find_element(By.ID, "downloadButton")

    def uploadBtn(self):
        return self.page_driver.find_element(By.ID, "fileinput")
