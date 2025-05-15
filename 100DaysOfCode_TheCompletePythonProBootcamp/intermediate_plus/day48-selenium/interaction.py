from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Firefox()
driver.get(URL)


fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")


fname.send_keys("nemo")
lname.send_keys("nobody")
email.send_keys("yyy@gmail.com")
button.click()






# nu_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# #nu_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# # nu_articles.click()

# searchbar = driver.find_element(By.NAME, value="search")

# searchbar.send_keys("Nier Automata", Keys.ENTER)