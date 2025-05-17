from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Set up chrome
# This code snippet is setting up Chrome options for the Selenium WebDriver.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# badoo time
URL ="https://badoo.com"
driver.get(URL)

# #Log in
log_in = driver.find_element(By.CSS_SELECTOR, value='div .button-group__item a')
time.sleep(2)
log_in.click()

# email field
time.sleep(1)
input_login = driver.find_element(By.TAG_NAME, value='input')
input_login.send_keys(os.environ["LOGIN"], Keys.ENTER)

# Don't send me your crap
time.sleep(1)
no_spam = driver.find_element(By.XPATH, value='//*[@id="app-root"]/div/div[4]/div/div/div/div[2]/div/div/div[2]/div[2]/button/span[1]/span/span')
no_spam.click()

# Deal with the captcha or verification code or whatever
input("Press ENTER after doing captcha/confirming your number or whatever else they want")

while True:
    time.sleep(2)
    driver.find_element(By.XPATH, value='//*[@id="page-container"]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div/button').click()
    time.sleep(2)
    
    try:
        nope = driver.find_element(By.XPATH, value='//*[@id="app-root"]/div/div[4]/div/div/div/div/div/div/div[2]/div[2]/button/span[1]/span/span')
        nope.click()
        time.sleep(3)
    except NoSuchElementException:
        continue
 
    
