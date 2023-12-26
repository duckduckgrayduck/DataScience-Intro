from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://the-internet.herokuapp.com/dynamic_loading')

example_1=browser.find_element(By.XPATH, "/html/body/div[2]/div/div/a[1]")
example_1.click()

try:
	start_button = browser.find_element(By.CSS_SELECTOR, "#start > button:nth-child(1)")
	start_button.click()
	element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "finish")))
	print(element.text)
except:
	print("failed")