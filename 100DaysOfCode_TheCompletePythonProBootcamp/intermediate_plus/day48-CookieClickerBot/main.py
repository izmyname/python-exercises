from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# The game's URL
URL = "https://orteil.dashnet.org/experiments/cookie/"

# Setup selenium webdriver with chrome and get url
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Set the time, when the game should end
stop_game = time.time() + 300

# Click on the cookie
cookie = driver.find_element(By.ID, value="cookie")

# Start the main game loop
cookie_time = True

while cookie_time:
    
    timeout = time.time() + 5 # we need it inside a while loop so it gets refreshed periodically
    
    while True:
        cookie.click()
        if time.time() > timeout:
            break

    # Get  my money
    money = driver.find_element(By.ID, value="money")
    my_money = int(money.text.replace(",", ""))

    #fetch the data from store and get the most expensive available element
    store = driver.find_elements(By.CSS_SELECTOR, "[class='']")
    store_list = [int(ele.text.split()[2].replace(",", "")) for ele in store]
    
    try:
        max_index = store_list.index(max(store_list))
    except ValueError:
        continue

    # check - whether I have enough money to buy an item
    if my_money >= max(store_list):
        store[max_index].click()
        
    if time.time() > stop_game:
        cookie_time = False
        cookies_second = driver.find_element(By.ID, value="cps")
        print(cookies_second.text)
