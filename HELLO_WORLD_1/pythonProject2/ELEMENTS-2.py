import time

from selenium import webdriver
from selenium.webdriver.common.by import By

my_chrome_driver = webdriver.Chrome()
my_chrome_driver.get("https://www.google.co.uk")
time.sleep(2)
my_chrome_driver.find_element(By.NAME,"q").send_keys("United States")
time.sleep(2)
my_chrome_driver.find_element(By.NAME,"btnK").click()
time.sleep(2)
#CSS -- tagname[element = value]
print(f"Searched for: {my_chrome_driver.find_element(By.XPATH,"//div[@role='heading'][normalize-space()='United States']").text}")
my_chrome_driver.maximize_window()
time.sleep(2)
my_chrome_driver.find_element(By.CSS_SELECTOR,"div[class='rfiSsc'] a:nth-child(2) div:nth-child(1)").click()
time.sleep(2)
my_chrome_driver.back()
time.sleep(2)
my_chrome_driver.back()
time.sleep(2)
my_chrome_driver.find_element(By.NAME,"q").send_keys("Britain")
time.sleep(2)
my_chrome_driver.find_element(By.NAME,'btnK').click()
time.sleep(2)
try:
    title = my_chrome_driver.find_element(By.XPATH, "//div[@class='QpPSMb']").text
    type1 = my_chrome_driver.find_element(By.CSS_SELECTOR,"div[class='iAIpCb PZPZlf'] span").text
    print(f"Searched for {title}\n type: {type1}")
    if title != "United Kingdom":
        print("Inside if block")
        raise Exception ("Sorry, searched for wrong item")
    else:
        print("Successfully found UK by searching for Britain")

except Exception as err:
    print(err)

finally:
    my_chrome_driver.find_element(By.XPATH, "//a[normalize-space()='Images']").click()
    time.sleep(2)
