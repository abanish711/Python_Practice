import time

import pytest
from selenium.webdriver.common.by import By
from PyTestGoogle import PageObjects


#EXAMPLE _ WHEN MULTIPLE TESTS USE THE FIXTURE SETUP
#FIXTURE DEFINED AT CLASS LEVEL
@pytest.mark.usefixtures("setup")
class TestGoogles:
    def test_googlea(self, setup):
        print("Initiating Google for test_google-2\nSearching for Germany")
        self.browser = setup
        home = PageObjects.Homepage()
        home.SearchBar(self.browser).send_keys("Germany")
        home.SearchBtn(self.browser).click()
        home.News(self.browser).click()
        time.sleep(2)
        self.browser.close()

    def test_googleb(self, setup):
        print("Initiating Google for test_google-3\nSearching for United States")
        self.browser = setup
        home = PageObjects.Homepage()
        home.SearchBar(self.browser).send_keys("United States")
        home.SearchBtn(self.browser).click()
        home.News(self.browser).click()
        time.sleep(2)
        self.browser.close()

    def test_googlec(self,setup):
        print("Initiating Google for test_google-4\nSearching for Japan")
        self.browser = setup
        home = PageObjects.Homepage()
        home.SearchBar(self.browser).send_keys("Japan")
        home.SearchBtn(self.browser).click()
        home.News(self.browser).click()
        time.sleep(2)
        self.browser.close()

