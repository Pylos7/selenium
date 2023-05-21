from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver')

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=options, service=service)

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
