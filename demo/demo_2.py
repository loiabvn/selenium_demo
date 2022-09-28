# Cmd: python3 demo/demo_2.py
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

# Connect to chrome via driver
file_path = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(executable_path=file_path + "/driver/chromedriver")

# Go to website
driver.get(url="https://rahulshettyacademy.com/angularpractice/")

# Input data to form
driver.find_element(by=By.XPATH, value="/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Le Trong Loi")
driver.find_element(by=By.NAME, value="email").send_keys("trongloi-le@am-bition.vn")
driver.find_element(by=By.ID, value="exampleInputPassword1").send_keys("123456")
driver.find_element(by=By.ID, value="exampleCheck1").click()
driver.find_element(by=By.ID, value="inlineRadio2").click()
driver.find_element(by=By.NAME, value="bday").send_keys("01/01/2000")
driver.find_element(by=By.XPATH, value="/html/body/app-root/form-comp/div/form/input").click()

print(driver.find_element(by=By.XPATH, value="/html/body/app-root/form-comp/div/div[2]/div").text)

# Wait 5s & close browser
time.sleep(5)
driver.quit()
