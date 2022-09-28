# Cmd: python3 demo/demo_5.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool


def test_selenium_grid(browser: str):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
    else:
        browser = 'chrome'
        options = webdriver.ChromeOptions()

    # Print to console
    print('Test on', browser)

    # Connect to Hub
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )

    try:
        driver.implicitly_wait(30)
        driver.maximize_window()  # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)
        driver.get("https://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("documentation")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    finally:
        driver.quit()


if __name__ == "__main__":
    pool = Pool(4)
    results = pool.map(test_selenium_grid, ['chrome', 'firefox'])
