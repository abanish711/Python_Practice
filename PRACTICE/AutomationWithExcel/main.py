from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import setup
import time
import excel_changes

browser = setup.Browser_driver("https://rahulshettyacademy.com/upload-download-test/index.html")
browser.driver.implicitly_wait(3)
homepage1 = setup.Homepage(browser.driver)
download_button = homepage1.downloadBtn()
download_button.click()
time.sleep(3)

downloaded_file = excel_changes.ExcelFile()
downloaded_file.readExcel("C:\\Users\\ABANISH KAR\\Downloads\\download.xlsx")
#
upload_button = homepage1.uploadBtn()
upload_button.send_keys("C:\\Users\\ABANISH KAR\\Downloads\\download.xlsx")

wait = WebDriverWait(browser.driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='Toastify__toast-body']/div[2]")))
print(browser.driver.find_element(By.XPATH,"//div[@class='Toastify__toast-body']/div[2]").text)
time.sleep(5)
