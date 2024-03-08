import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

my_browser_handle = webdriver.Chrome()
my_browser_handle.get("https://www.trainline.com")
time.sleep(1)
my_browser_handle.find_element(By.ID, "from.search_2024-02-21T05").send_keys("lon")
time.sleep(2)
stations = my_browser_handle.find_elements(By.CSS_SELECTOR, "li[role='option'] div span ")
for station in stations:
    print(station.text)
    if "Liverpool" in station.text:
        print(f"Selecting station {station.text}\n")
        station.click()
        break

time.sleep(2)
