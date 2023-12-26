from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start the webdriver
browser = webdriver.Firefox()
# Direct to the FOMB page
browser.get('https://juntasupervision.pr.gov/documents/')
# Select the display dropdown and click on it. 
dropdown = browser.find_element(By.CSS_SELECTOR, "#docsDataTable_length > label:nth-child(1) > select:nth-child(1)")
dropdown.click()
# Find the option to show 100 results per page, click it. 
option_100 = browser.find_element(By.CSS_SELECTOR, "#docsDataTable_length > label:nth-child(1) > select:nth-child(1) > option:nth-child(4)")
option_100.click()

links = []

# Find the even rows, get the links. 
evens = browser.find_elements(By.CLASS_NAME, "even")
for row in evens:
	# Find the <a> element within the row
	link_element = row.find_element(By.TAG_NAME, 'a')
	# Get the value of the 'href' attribute
	href_value = link_element.get_attribute('href')
	# Print or use the href value as needed
	links.append(href_value)

# Find the odd rows, get the links.
odds = browser.find_elements(By.CLASS_NAME, "odd")
for row in odds:
	# Find the <a> element within the row
	link_element = row.find_element(By.TAG_NAME, 'a')
	# Get the value of the 'href' attribute
	href_value = link_element.get_attribute('href')
	# Print or use the href value as needed
	links.append(href_value)

print(len(links)) # Should be 100 in total, 50 from even rows and 50 from odd rows. 

# Clicks on the next button. 
next_button = browser.find_element(By.CSS_SELECTOR, "#docsDataTable_next")
next_button.click()

