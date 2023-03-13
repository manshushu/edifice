# Importing required libraries
from selenium import webdriver

# Creating a new instance of Firefox driver
driver = webdriver.Firefox()

# Navigating to the website
driver.get("https://www.google.com")

# Finding input field using its name attribute
input_element = driver.find_element_by_name("q")

# Typing in the search query
input_element.send_keys("Selenium")

# Submitting the form
input_element.submit()

# Closing the browser session
driver.quit()
