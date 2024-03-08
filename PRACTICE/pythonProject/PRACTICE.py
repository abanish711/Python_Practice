import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

my_browser_options = webdriver.ChromeOptions()
my_browser_options.add_argument("--start-maximized")
my_chrome_driver = webdriver.Chrome(options=my_browser_options)
my_chrome_driver.implicitly_wait(3)
my_chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")

my_chrome_driver.find_element(By.LINK_TEXT,"Shop").click()

items = my_chrome_driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for i in items:
    #print(i.text)
    if "Blackberry" in i.text:
        print(i.text)
        print(i.find_element(By.XPATH,"//div[@class='card-footer']/button").text)
        i.find_element(By.XPATH,"div/button").click()
        break

my_chrome_driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
my_chrome_driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
my_chrome_driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")
# EXPLICIT WAIT USAGE
# WAIT UNTIL THIS PARTICULAR ELEMENT APPEARS ON THE PAGE
# 1) CREATE OBJECT OF WebDriverWait class --> Only this object can be used for explicit wait (IMPORT WebDriverWait for this)
# 2) CALL 'until' FUNCTION OF WAIT OBJECT --> NEED TO CALL USING 'EXPECTED CONDITION' FUNCTION (IMPORT expected_conditions for this)
# 3) EXPECTED CONDITION HAS MANY VARIANTS to FIND WHICH SPECIFIC CONDITION WE NEED TO WAIT FOR
wait_object = WebDriverWait(my_chrome_driver, 15)
wait_object.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))
countries = my_chrome_driver.find_elements(By.XPATH,"//div[@class='suggestions']/ul")
#time.sleep(2)
for country in countries:
    print(country.text)
    if country.text == 'India':
        country.click()
        break

my_chrome_driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
my_chrome_driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
assert "Success" in my_chrome_driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(my_chrome_driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text)

time.sleep(1)


