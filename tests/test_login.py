# Selenium + python Unitest (pytest)
# Cmd: pytest tests/test_login.py --html=report.html -s
import time

import pytest
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class TestLogin(BaseClass):

    def test_tc1(self):
        self.driver.get(url="https://practicetestautomation.com/practice-test-login/")

        self.driver.find_element(by=By.ID, value="username").send_keys("student")
        self.driver.find_element(by=By.ID, value="password").send_keys("Password123")
        self.driver.find_element(by=By.ID, value="submit").click()
        message = self.driver.find_element(by=By.XPATH, value='//*[@id="loop-container"]/div/article/div[1]/h1').text
        time.sleep(5)
        self.driver.get_screenshot_as_file(filename="../reports/screenshot.png")
        assert message == 'Logged In Successfully'

    def test_tc2(self):
        logger = self.getLogger()
        logger.info("execute test_tc2")
        assert True

    def test_tc3(self):
        logger = self.getLogger()
        logger.info("execute test_tc3")
        assert True
