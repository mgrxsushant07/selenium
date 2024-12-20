###Open amazom.com and search Rich dad and poor dad

from selenium import webdriver
import time
browser=webdriver.Chrome()  
browser.get("https://www.amazon.com")
time.sleep(10)
browser.find_element_by_name("field-keywords").send_keys("Rich Dad Poor Dad")
browser.find_element_by_id("nav-search-submit-button").click()