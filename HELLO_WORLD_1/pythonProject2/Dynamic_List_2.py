import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

my_browser_driver = webdriver.Chrome()
# IMPLICIT WAIT USAGE --> MAX WAIT TIME (GLOBAL)
my_browser_driver.implicitly_wait(5)
my_browser_driver.get("https://www.makemytrip.com")
my_browser_driver.maximize_window()
my_browser_driver.find_element(By.ID, "fromCity").send_keys("Ban")
fromairports = my_browser_driver.find_elements(By.CSS_SELECTOR, "ul[role = 'listbox'] li")
print(f"Total items in dropdpwn for 'FROM' airport: {len(fromairports)}")
for a in fromairports:
    if "Bangkok" in a.text:
        print(f"-------------------------------------Selecting {a.text} as 'FROM' airport\n")
        a.click()
        break

my_browser_driver.find_element(By.ID, "toCity").send_keys("Del")
to_airports = my_browser_driver.find_elements(By.CSS_SELECTOR, "ul[role = 'listbox'] li")
print(f"Total items in dropdpwn for 'TO' airport: {len(fromairports)}")
for a in to_airports:
    if "Delhi" in a.text:
        print(f"-------------------------------------Selecting {a.text} as 'TO' airport\n")
        a.click()
        break
my_browser_driver.find_element(By.XPATH, "//div[@aria-label='Sun Mar 03 2024']//p[contains(text(),'3')]").click()
Day = my_browser_driver.find_element(By.CSS_SELECTOR, "p[data-cy='departureDate'] span[class='font30 latoBlack']").text
Month = my_browser_driver.find_element(By.XPATH, "//span[normalize-space()='Mar']").text
Year = my_browser_driver.find_element(By.XPATH, "//span[@class='shortYear']").text
print(f"Selected Date: {Day} {Month} {Year} ")
my_browser_driver.find_element(By.CSS_SELECTOR, "li[data-cy='roundTrip'] span[class='tabsCircle appendRight5']").click()
time.sleep(2)
my_browser_driver.find_element(By.CSS_SELECTOR, ".primaryBtn.font24.latoBold.widgetSearchBtn").click()
# EXPLICIT WAIT USAGE
# WAIT UNTIL THIS PARTICULAR ELEMENT APPEARS ON THE PAGE
# 1) CREATE OBJECT OF WebDriverWait class --> Only this object can be used for explicit wait (IMPORT WebDriverWait for this)
# 2) CALL 'until' FUNCTION OF WAIT OBJECT --> NEED TO CALL USING 'EXPECTED CONDITION' FUNCTION (IMPORT expected_conditions for this)
# 3) EXPECTED CONDITION HAS MANY VARIANTS to FIND WHICH SPECIFIC CONDITION WE NEED TO WAIT FOR
wait_object = WebDriverWait(my_browser_driver, 15)
wait_object.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'filterWrapper']")))
my_browser_driver.fullscreen_window()
time.sleep(3)
my_browser_driver.find_element(By.XPATH,"//button[@class='button buttonSecondry buttonBig fontSize12 relative']").click()
time.sleep(1)
my_browser_driver.find_element(By.XPATH,"(//input[@id='listingFilterCheckbox'])[1]").click()
# XPATH for LARGER SECTION  - //div[@class='makeFlex']
# XPATH for SELECT BUTTON - //button[@class="ViewFareBtn"]
time.sleep(2)
airlines = my_browser_driver.find_elements(By.XPATH,"//div[@class='makeFlex']")
for a in airlines:
    print(a.text)
    #print(a.find_element(By.CLASS_NAME,"boldFont blackText airlineName").text)
