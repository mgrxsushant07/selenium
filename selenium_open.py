from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome browser
browser = webdriver.Chrome()

# Open pip.com
browser.get('https://pypi.org//')

# Search for "selenium" in the search bar
searchbox = browser.find_element(By.NAME, 'q')
searchbox.send_keys('selenium')
searchbox.submit()

# Wait for a few seconds to see the results
time.sleep(50)

# Close the browser
browser.quit()