import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

my_chrome_browser = webdriver.Chrome()
my_chrome_browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")
my_chrome_browser.maximize_window()
my_chrome_browser.implicitly_wait(10)

my_chrome_browser.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
expected_items = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

################################COUNT CHECK
selected_items = []
items = my_chrome_browser.find_elements(By.XPATH,"//div[@class='product'] /h4")
for i in items:
    print(f"Adding {i.text}")
    selected_items.append(i.text)

print(f"Expected count is 3. Total items selected on screen are {len(selected_items)}")

################################COUNT CHECK

my_chrome_browser.find_element(By.XPATH,"//button[@type = 'submit']")
buttons = my_chrome_browser.find_elements(By.XPATH,"//div[@class='product'] /div / button")
for b in buttons:
    b.click()
my_chrome_browser.find_element(By.XPATH,"//img[@alt='Cart']").click()
my_chrome_browser.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()
my_chrome_browser.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
my_chrome_browser.find_element(By.CSS_SELECTOR,".promoBtn").click()
# EXPLICIT WAIT USAGE
# WAIT UNTIL THIS PARTICULAR ELEMENT APPEARS ON THE PAGE
# 1) CREATE OBJECT OF WebDriverWait class --> Only this object can be used for explicit wait (IMPORT WebDriverWait for this)
# 2) CALL 'until' FUNCTION OF WAIT OBJECT --> NEED TO CALL USING 'EXPECTED CONDITION' FUNCTION (IMPORT expected_conditions for this)
# 3) EXPECTED CONDITION HAS MANY VARIANTS to FIND WHICH SPECIFIC CONDITION WE NEED TO WAIT FOR
wait_object = WebDriverWait(my_chrome_browser, 15)
wait_object.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
time.sleep(3)
total_amount = float(my_chrome_browser.find_element(By.CSS_SELECTOR,".totAmt").text)
discount_amount = float(my_chrome_browser.find_element(By.CSS_SELECTOR,".discountAmt").text)
expected_discount = float(my_chrome_browser.find_element(By.CSS_SELECTOR,".discountPerc").text.rstrip('%'))/100
actual_discount = round((1-(discount_amount/total_amount)),2)
print(f"Total amount was {total_amount} and discounted amount was {discount_amount}")
print(f"Discount provided is: {actual_discount*100}% and Expected discount was {expected_discount*100}%")
if actual_discount == expected_discount:
    print(f"SUCCESS: Actual discount matches expected discount")
for i in range(0,3):
    print(f"Expected:{expected_items[i]} Actual: {selected_items[i]}")


