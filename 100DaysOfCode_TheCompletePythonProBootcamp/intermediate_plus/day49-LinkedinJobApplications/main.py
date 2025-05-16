from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Set up chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Go to linkedin
URL = "https://www.linkedin.com/jobs/search/?currentJobId=4226247182&f_AL=true&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&spellCorrectionEnabled=true"
driver.get(URL)

# Autologin 
sign_in = driver.find_element(By.CLASS_NAME, value="sign-in-modal")
name = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
passwd = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
final_sign_in = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')

time.sleep(5)
sign_in.click()    
name.send_keys(os.environ["LOGIN"])
passwd.send_keys(os.environ["PASSWD"])
final_sign_in.click()

# CAPTCHA - Solve Puzzle Manually
input("Screw you, captcha")


# Find and visit all the companies' pages 
companies_list = driver.find_elements(By.CLASS_NAME, value="job-card-job-posting-card-wrapper")
for company in companies_list:
    company.click()

    # Save the job and follow the company
    time.sleep(4)
    save_job = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    follow_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/section/section/div[1]/div[1]/button/span')

    time.sleep(6)
    save_job.click()
    driver.execute_script("arguments[0].scrollIntoView();", follow_button)

    time.sleep(2)
    follow_button.click()

