import time

from selenium import webdriver

# You need browser specific driver to create an object of that driver. Here Selenium is downloading the browser
# driver from internet on its own.
# If Selemium can't get the browser driver on its own due to firewall issues or lack of rights of the user etc,
# then you need to download the driver for the browser manually and pass that driver as argument to create your driver
# object.

my_edge_driver = webdriver.Edge()
my_chrome_driver = webdriver.Chrome()
my_chrome_driver.get("https://www.google.com")
my_chrome_driver.minimize_window()
time.sleep(5)
print(my_chrome_driver.title)
print(my_chrome_driver.current_url)
my_chrome_driver.minimize_window()
my_edge_driver.get("https://www.facebook.com")

