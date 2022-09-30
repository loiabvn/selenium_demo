import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help='chrome|firefox')


@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.option.browser
    options = webdriver.ChromeOptions()
    if browser == 'chrome':
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        options = webdriver.ChromeOptions()
    elif browser == 'firefox':
        # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        options = webdriver.FirefoxOptions()
    else:
        pytest.skip()

    driver = webdriver.Remote(
        command_executor="http://selenium-hub:4444/wd/hub",
        options=options
    )

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
