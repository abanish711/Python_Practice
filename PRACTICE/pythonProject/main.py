import time

from selenium import webdriver
from selenium.webdriver.common.by import By

my_chrome_driver = webdriver.Chrome()
my_chrome_driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
my_chrome_driver.maximize_window()
time.sleep(2)
radios = my_chrome_driver.find_elements(By.XPATH, "//input[@type='radio']")
for radio in radios:
    if radio.get_attribute("value") == 'radio3':
        radio.click()
        print(f"Clicked on {radio.get_attribute("value")}")
        assert radio.is_selected()
        break
time.sleep(1)


//div[@id='flight_list_item_RKEY:b64fb4da-6f71-4025-85c6-b3188542be88:16_0']//button[@class='ViewFareBtn'][normalize-space()='SELECT']