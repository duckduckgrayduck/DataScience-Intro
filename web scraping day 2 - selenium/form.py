from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://the-internet.herokuapp.com/login')

user_field= browser.find_element(By.ID, 'username')
user_field.click() 
user_field.send_keys('tomsmith')

pass_field = browser.find_element(By.ID, 'password')
pass_field.click()
pass_field.send_keys("SuperSecretPassword!")

submit_button = browser.find_element(By.CLASS_NAME, 'radius')
submit_button.click()

browser.close()
