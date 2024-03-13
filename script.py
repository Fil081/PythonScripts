from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')



service = Service(ChromeDriverManager().install())

def login_and_like(username, password):
    driver = webdriver.Chrome(service=service)

# Open Truth Social Login papge
    driver.get("https://truthsocial.com/login")

    try:

        time.sleep(10)
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
   # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//element_after_login')))

        sign_in_button = driver.find_element(By.XPATH, "//button[.//span[text()='Sign in']]")
        sign_in_button.click()
        time.sleep(10)
    #Login Successful.
    #Take the link from the comment.
        newUrl="https://truthsocial.com/@maganewsss2024/posts/112084939871448005"
        driver.get(newUrl)
        time.sleep(20)
        like_button = driver.find_element(By.XPATH, "//button[@title='Like']")
        time.sleep(20)
        like_button.click()
        time.sleep(20)





    except NoSuchElementException:
        print("Element not found on the page")
    except TimeoutException:
        print("Page load timed out")
    finally:
        driver.quit()

# Read credentials from file
with open('credentials.txt', 'r') as file:
    for line in file:
        username, password = line.strip().split(',')
        login_and_like(username, password)


