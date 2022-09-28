# Can't log in to google auth
# Cmd: python3 demo/demo_oauth2.py

from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium_stealth import stealth

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# from msvcrt import getch

# def white_password(prompt):       # A simple approach to Secure password input.!
#     print(prompt, end='', flush=True)
#     buf = b''
#     while True:
#         ch = getch()
#         if ch in {b'\n', b'\r', b'\r\n'}:  # End Of Line or Carriage Return
#             print('')
#             break
#         elif ch == b'\x08':  # Backspace
#             buf = buf[:-1]
#             print(f'\r{(len(prompt) + len(buf) + 1) * ""}\r{prompt}{"" * len(buf)}', end='', flush=True)
#         elif ch == b'\x03':  # Copy or Ctrl + C
#             raise KeyboardInterrupt
#         else:
#             buf += ch
#             print('', end='', flush=True)       # Prints nothing instead of Password on the screen
#     return buf.decode(encoding='utf-8')

def login(username, password):  # Logs in the user
    driver.get("https://stackoverflow.com/users/login")
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@id="openid-buttons"]/button[1]'))).click()

    try:
        WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located(
            (By.ID, "Email"))).send_keys(username)  # Enters username
    except TimeoutException:
        del username
        driver.quit()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/form/div/div/input"))).click()  # Clicks NEXT
    sleep(0.5)

    try:
        try:
            WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located(
                (By.ID, "password"))).send_keys(password)  # Enters decoded Password
        except TimeoutException:
            driver.quit()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
            (By.ID, "submit"))).click()  # Clicks on Sign-in
    except TimeoutException or NoSuchElementException:
        print('\nUsername/Password seems to be incorrect, please re-check\nand Re-Run the program.')
        del username, password
        driver.quit()

    try:
        WebDriverWait(driver, 60).until(lambda webpage: "https://stackoverflow.com/" in webpage.current_url)
        print('\nLogin Successful!\n')
    except TimeoutException:
        print('\nUsername/Password seems to be incorrect, please re-check\nand Re-Run the program.')
        del username, password
        driver.quit()


USERNAME = input("User Name : ")
# PASSWORD = white_password(prompt="Password  : ")      # A custom function for secured password input, explained at end.
PASSWORD = input("Password  : ")  # A custom function for secured password input, explained at end.

# Expected and required arguments added here.
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Assign drivers here.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

stealth(driver,
        user_agent='DN',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )  # Before Login, using stealth

login(USERNAME, PASSWORD)  # Call login function/method

stealth(driver,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )  # After logging in, revert user agent to normal.

# Redirecting to Google Meet Web-Page
sleep(2)
driver.execute_script("window.open('https://google.com')")
driver.switch_to.window(driver.window_handles[1])  # Redirecting to required from stackoverflow after logging in
driver.switch_to.window(driver.window_handles[0])  # This switches to stackoverflow website
driver.close()  # This closes the stackoverflow website
driver.switch_to.window(driver.window_handles[0])  # Focuses on present website
