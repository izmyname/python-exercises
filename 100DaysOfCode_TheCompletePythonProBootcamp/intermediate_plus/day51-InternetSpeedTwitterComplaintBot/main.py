from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Add some constants
PROMISED_UP = 10
PROMISED_DOWN = 1500
SPEEDTEST ="https://www.speedtest.net/"
TWITTER = "https://x.com"

# Create a class and methods
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = self.setup_chrome()
        self.up = 0
        self.down = 0
        
    def setup_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        return webdriver.Chrome(options=chrome_options)
        
    def get_internet_speed(self):
        self.driver.get(SPEEDTEST)
        time.sleep(2)
        reject_cookies = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
        reject_cookies.click()
        time.sleep(1)
        start_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        start_button.click()
        time.sleep(46)
        dismiss_notification = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[8]/div/div/div[2]/a')
        dismiss_notification.click()
        download_speed = self.driver.find_element(By.XPATH, value ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upload_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)
    
    def tweet_at_provider(self):
        time.sleep(2)
        self.driver.get(TWITTER)
        time.sleep(2)
        no_cookie = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div/span/span')
        no_cookie.click()
        time.sleep(2)
        signin = self.driver.find_element(By.CSS_SELECTOR, value="div a[href='/login']")
        signin.click()
        time.sleep(4)
        log_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        log_input.send_keys(os.environ["TWITTER_NAME"], Keys.ENTER)
        time.sleep(2)
        username_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_input.send_keys(os.environ["TWITTER_USERNAME"], Keys.ENTER)
        time.sleep(1)
        passwd_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passwd_input.send_keys(os.environ["TWITTER_PASSWD"], Keys.ENTER)
        time.sleep(3)
        
        if PROMISED_UP < self.up or PROMISED_DOWN < self.down:
            time.sleep(1)
            twitter_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
            twitter_input.send_keys(f"Dear provider - why is my internet speed is {self.down} down/{self.up} up, when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up? ")
            time.sleep(1)
            twitter_post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            twitter_post.click()
        
# Create an objet and call the methods
twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
