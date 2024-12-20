from selenium import webdriver
import time
browser = webdriver.Edge()
browser.get('http://amazon.com/')

book_name = "Rich Dad Poor Dad"
searchbox = browser.find_element(by='name', value='field-keywords')
searchbox.send_keys(book_name)
searchbox.submit()
time.sleep(50)

### Open Amazon.com using Selenium.
# 2-3 Min
### Open Amazon.com and Search For Rich Dad Poor Dad