# Cmd: python3 demo/demo_1.py
import time
import os

from selenium import webdriver

# Connect to chrome via driver
file_path = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(executable_path=file_path + "/driver/chromedriver")

# Go to website
driver.get(url="https://rahulshettyacademy.com/angularpractice/")

# Get website info
print(driver.title)
print(driver.current_url)

# Wait 5s & close browser
time.sleep(5)
driver.quit()
