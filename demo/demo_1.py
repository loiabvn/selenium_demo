import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="driver/chromedriver")

driver.get(url="https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
print(driver.current_url)

time.sleep(5)
driver.quit()
