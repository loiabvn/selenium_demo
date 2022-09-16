# Selenium + python Unitest (pytest)
# Execute command: pytest demo_4_2.py --verbose --capture=no
import sys
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class TestClass:

    @classmethod
    def setup_class(cls):
        print("\n===== BEGIN =====")
        print("Setup class: {} execution".format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        print("\nTeardown class: {} execution".format(cls.__name__))
        print("===== END =====")

    def setup_method(self, method):
        print("\n\tsetup method for tc: {}".format(method.__name__))

    def teardown_method(self, method):
        print("\tteardown method for tc: {}".format(method.__name__))

    @pytest.fixture()
    def data_ok(self):
        print('\tsetup data_ok')
        data = ['username_correct', 'password_correct']
        yield data
        print('\tteardown data_ok')

    @pytest.fixture()
    def data_fail(self):
        print('\tsetup data_fail')
        data = ['username_incorrect', 'password_incorrect']
        yield data
        print('\tteardown data_fail')

    @pytest.fixture()
    def browser(self):
        print('\tsetup browser')

        # Initialize chrome driver
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # Wait implicitly for elements to be ready before attempting interactions
        driver.implicitly_wait(10)

        # Return the driver object at the end of setup
        yield driver

        # For cleanup, quit the driver
        driver.quit()

        print('\tquit browser')

    def test_tc1(self, data_ok, browser):
        print('\ttc_content_1', data_ok)
        try:
            browser.get('https://lambdatest.github.io/sample-todo-app/')
            browser.maximize_window()

            browser.find_element(By.NAME, "li1").click()
            browser.find_element(By.NAME, "li2").click()

            title = "Sample page - lambdatest.com"
            assert title == browser.title

            sample_text = "Happy Testing at LambdaTest"
            email_text_field = browser.find_element(By.ID, "sampletodotext")
            email_text_field.send_keys(sample_text)
            sleep(3)

            browser.find_element(By.ID, "addbutton").click()
            sleep(3)

            output_str = browser.find_element(By.NAME, "li6").text
            sys.stderr.write(output_str)
        except Exception as e:
            print(e)
        finally:
            browser.close()

    def test_tc2(self, data_fail):
        print('\ttc_content_2', data_fail)
        assert True

    def test_tc3(self, data_fail):
        print('\ttc_content_3', data_fail)
        assert True
