import time

from selenium import webdriver
from selenium.webdriver.common.by import By

my_chrome_driver = webdriver.Chrome()
my_chrome_driver.get("https://www.google.co.uk")
time.sleep(2)
my_chrome_driver.find_element(By.NAME, "q").send_keys("Britain")
time.sleep(3)
my_chrome_driver.find_element(By.NAME,"btnK").click()
time.sleep(3)
my_chrome_driver.maximize_window()
time.sleep(3)
my_chrome_driver.back()
time.sleep(3)
my_chrome_driver.find_element(By.NAME,"q").send_keys("United Kingdom")
time.sleep(3)
my_chrome_driver.find_element(By.NAME,"btnK").click()
time.sleep(3)
# XPATH for LABEL -> //ELEMENT_TAG[@ANY ATTRIBUTE IN THAT TAG = 'VALUE OF THAT ATTRIBUTE']
print(my_chrome_driver.find_element(By.XPATH,"//div[@data-attrid = 'title']").text)
time.sleep(3)
# XPATH for NEWS LINK -> //ELEMENT_TAG[@ANY ATTRIBUTE IN THAT TAG = 'VALUE OF THAT ATTRIBUTE']
my_chrome_driver.find_element(By.CLASS_NAME,"FMKtTb").click()
#time.sleep(3)
#my_chrome_driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(11) > div:nth-child(1) > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > span:nth-child(1)").click()
