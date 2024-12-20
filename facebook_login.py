from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the web driver (ensure chromedriver is installed and in PATH)
service = Service('path_to_chromedriver')  # Replace with the actual path to chromedriver
driver = webdriver.Chrome(service=service)

try:
    # Open Facebook login page
    driver.get('https://www.facebook.com/')

    # Maximize browser window
    driver.maximize_window()

    # Locate and interact with the email and password fields
    email_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    # Input your credentials
    email = "your_email@example.com"  # Replace with your Facebook email
    password = "your_password"        # Replace with your Facebook password

    email_field.send_keys(email)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to allow login to process
    time.sleep(5)

    # Check if login was successful (look for a specific element on the homepage)
    if "Facebook" in driver.title:
        print("Login successful!")
    else:
        print("Login failed. Please check your credentials.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after a delay
    time.sleep(5)
    driver.quit()
