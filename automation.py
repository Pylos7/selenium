from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver')

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=options, service=service)

chrome_browser.maximize_window()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

button_text = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")

print(button_text.get_attribute('innerHTML'))