import time

from selenium import webdriver
from selenium.webdriver.common.by import By

my_browser_handle = webdriver.Firefox()
my_browser_handle.get("https://the-internet.herokuapp.com/windows")
my_browser_handle.implicitly_wait(5)
my_browser_handle.maximize_window()
my_browser_handle.find_element(By.LINK_TEXT, "Click Here").click()
opened_browsers = my_browser_handle.window_handles  # THIS RETURNS ALL WINDOW HANDLES OPENED BY THIS BROWSER
print(f"Total {len(opened_browsers)} windows opened in t1his session by my_browser_handle")
my_browser_handle.switch_to.window(opened_browsers[1])
print(my_browser_handle.find_element(By.TAG_NAME, "h3").text)
my_browser_handle.close()
my_browser_handle.switch_to.window(opened_browsers[0])
print(my_browser_handle.find_element(By.TAG_NAME, "h3").text)
time.sleep(3)
my_browser_handle.close()
