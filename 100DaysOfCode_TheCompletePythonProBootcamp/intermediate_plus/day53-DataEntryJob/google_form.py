from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

class GoogleForm:
    def __init__(self, google_form):
        self.google_form = google_form
        self.driver = self.setup_chrome()
        
    def setup_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=chrome_options)
    
    def fill_form(self, house_address, house_price, house_links):
        self.driver.get(self.google_form)
        time.sleep(3)
        addr = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        addr.send_keys(house_address)
        price = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price.send_keys(house_price)
        link = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link.send_keys(house_links)
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        button.click()
        time.sleep(2)
        return_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        return_button.click()

