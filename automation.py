from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#https://selenium-python.readthedocs.io/locating-elements.html

# Set up test service
service = Service(executable_path='./chromedriver')

# Set pages optins to keep page open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=options, service=service)

# Open test page in browser
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# Find button element and print its Text
show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
# print(show_message_button.get_attribute('innerHTML'))

# See if element is in pages source
assert 'Show Message' in chrome_browser.page_source

# Send keystrokes to form
user_message = chrome_browser.find_element(By.ID, "user-message")
user_button = chrome_browser.find_element(By.CSS_SELECTOR, '#gettotal > .btn') #
print(user_button)
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')

# Simulate a click
show_message_button.click()

# Output Message
output_message = chrome_browser.find_element(By.ID, 'display')
print(output_message.get_attribute('innerHTML'))

chrome_browser.close() #.quit()  -  For closing the entire webdriver