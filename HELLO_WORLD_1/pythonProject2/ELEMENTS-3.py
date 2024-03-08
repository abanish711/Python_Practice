import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

my_browser_handle = webdriver.Chrome()
my_browser_handle.get("https://www.google.co.uk")
time.sleep(1)
my_browser_handle.maximize_window()
my_browser_handle.find_element(By.NAME, 'q').send_keys("Europe")
time.sleep(1)
my_browser_handle.find_element(By.NAME,'btnK').click()
time.sleep(1)
my_browser_handle.find_element(By.LINK_TEXT,"News").click()
time.sleep(1)
my_browser_handle.find_element(By.LINK_TEXT,"Maps").click()
time.sleep(1)
###################################################################################################################
# To automate action on a static drop down, you need to create an object of 'Select' class.
# That object will represent the dropdown list.
# Then you can use various functions of select class object to test that dropdown list.
# Note: Need to import 'from selenium.webdriver.support.select import Select' to create object of Select class
my_browser_handle.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(1)
dropdown = Select(my_browser_handle.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
time.sleep(1)
dropdown.select_by_visible_text("Male")
time.sleep(1)
###################################################################################################################


