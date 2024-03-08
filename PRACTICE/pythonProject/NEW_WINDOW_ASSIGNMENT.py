import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

my_browser_handle = webdriver.Chrome()
my_browser_handle.get("https://www.rahulshettyacademy.com/loginpagePractise/")
my_browser_handle.implicitly_wait(5)
my_browser_handle.maximize_window()

my_browser_handle.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
opened_browsers = my_browser_handle.window_handles  # THIS RETURNS ALL WINDOW HANDLES OPENED BY THIS BROWSER
print(f"Total {len(opened_browsers)} windows opened in this session by my_browser_handle")

my_browser_handle.switch_to.window(opened_browsers[1])

text = my_browser_handle.find_element(By.XPATH,"//div[@id='interview-material-container'] /div /div[2]").text
splitted_words = text.split()
email = ""
for w in splitted_words:
    if('@' in w):
        email = w
        break
print(f"Email: {email}")
my_browser_handle.close()
my_browser_handle.switch_to.window(opened_browsers[0])

my_browser_handle.find_element(By.ID, "username").send_keys(email)
my_browser_handle.find_element(By.ID, "password").send_keys("123456abcdf")
my_browser_handle.find_element(By.ID, "terms").click()
my_browser_handle.find_element(By.ID,"signInBtn").click()
time.sleep(2)
# EXPLICIT WAIT USAGE
# WAIT UNTIL THIS PARTICULAR ELEMENT APPEARS ON THE PAGE
# 1) CREATE OBJECT OF WebDriverWait class --> Only this object can be used for explicit wait (IMPORT WebDriverWait for this)
# 2) CALL 'until' FUNCTION OF WAIT OBJECT --> NEED TO CALL USING 'EXPECTED CONDITION' FUNCTION (IMPORT expected_conditions for this)
# 3) EXPECTED CONDITION HAS MANY VARIANTS to FIND WHICH SPECIFIC CONDITION WE NEED TO WAIT FOR
#wait_obj = WebDriverWait(my_browser_handle,10)
#wait_obj.until(expected_conditions.presence_of_element_located((By.XPATH,"//form[@id='login-form']/div[1]")))
print(f"Error: {my_browser_handle.find_element(By.XPATH,"//form[@id='login-form']/div[1]").text}")
time.sleep(3)





