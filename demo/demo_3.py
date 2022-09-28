# Cmd: python3 demo/demo_3.py
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Connect to chrome via driver
file_path = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(executable_path=file_path + "/driver/chromedriver")

# Go to website
driver.get(url="https://rahulshettyacademy.com/angularpractice/")

# 1. Scroll to bottom
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 2. Wait the element visible
driver.find_element(by=By.XPATH, value="/html/body/app-root/form-comp/div/form/input").click()
wait = WebDriverWait(driver, 10)
result_message = wait.until(
        # presence_of_element_located: This does not necessarily mean that the element is visible
        # visibility_of_element_located: Visibility means that the element is not only displayed
        #                                  but also has a height and width that is greater than 0
        # element_to_be_clickable: Which is an expectation for checking an element is visible
        #                          and enabled such that you can click it
        EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div"))
    ).text
print(result_message)

# 3. Screenshot
driver.get_screenshot_as_file(filename="screenshot.png")

# 4. Set window size
driver.set_window_size(300, 500)

# More: https://selenium-python.readthedocs.io/api.html

# Wait 5s & close browser
time.sleep(5)
driver.quit()
