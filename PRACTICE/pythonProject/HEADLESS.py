#Headless Window is a mode where test script runs without invoking the browser
#It is expected to be faster than running the steps with invoking the browser
from selenium import webdriver

chrome_options = webdriver.ChromeOptions() #CREATE THE OPTIONS OBJECT
chrome_options.add_argument("--start-maximized") `
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
my_chrome_driver = webdriver.Chrome(options=chrome_options) #LINK THE OPTIONS OBJECT WITH BROWSER OBJECT

my_chrome_driver.get("https://www.google.co.uk")
print(my_chrome_driver.title)

