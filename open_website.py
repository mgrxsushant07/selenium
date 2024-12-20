###write a program to open amazon.com uisng selenium
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://www.amazon.com")
time.sleep(10)