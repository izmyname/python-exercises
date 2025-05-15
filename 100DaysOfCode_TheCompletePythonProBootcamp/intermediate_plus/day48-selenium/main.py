from selenium import webdriver
from selenium.webdriver.common.by import By


# URL="https://www.amazon.de/-/en/Diohauxi-Interchangeable-Figures-Chassis-Ornament/dp/B0DXPXPRGX/ref=sr_1_7?crid=MEAJLK290NQI&dib=eyJ2IjoiMSJ9.vIs0TiZDd0m468QuAYLqdY2NfYxQc6CYAFxsOjPvUWI-yNhmx-rjAqrRZ45srtjaadaooSAlKQbthw1WOAN7xs6i05l0uqwynX4qorVaPLdiAYoLYpwBICVbOfdVmODDIBV9ZD9IMn56XRSXPQ3Pjau5YP1BjIPmRQLmCC8mCE5lsW16pbzft9gZIWQQq9wpeiVwVX_xP9CSA3AiBVFwgyw53KLzbaOTS4EzV8dh9pYUP87ldgMsIRjZKK0X1276FzhfZ2s8yQxzcx0v5jcOigBT38eNVIMQwj3t9Eia0GY.odqf2Cgp7FY0FkZNkljHhYcmgQrH72t6OVKjKz_nwQ0&dib_tag=se&keywords=2b%2Bfigurine&qid=1747218436&sprefix=2b%2Bfigurine%2Caps%2C207&sr=8-7&th=1"
URL = "https://www.python.org"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# price_eur = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_eur.text}.{price_cent.text}")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

py_events = {}

python_events_time = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
python_events_name = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

python_time_decoded = [elem.text for elem in python_events_time]
python_name_decoded = [elem.text for elem in python_events_name]

for n in range(len(python_events_name)):
    py_events[n]={"time": python_time_decoded[n], "name": python_name_decoded[n]}
    
print(py_events)



driver.quit()