from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

start_time=time.time()

def grab_links(browser):
    links = []
    link_elements = browser.find_elements(By.CSS_SELECTOR, "#docsDataTable tbody tr a")
    links = [link.get_attribute('href') for link in link_elements]
    return links

links = []
# Start the webdriver
options = Options()
options.add_argument("--headless")
prefs = {"profile.managed_default_content_settings.images": 2}
options.set_preference("permissions.default.image", 2)
browser = webdriver.Firefox(options=options)
browser.get('https://juntasupervision.pr.gov/documents/')

last_dropdown_item=browser.find_element(By.CSS_SELECTOR, "#docsDataTable_length > label:nth-child(1) > select:nth-child(1) > option:nth-child(4)")

browser.execute_script("arguments[0].innerText = '4572'", last_dropdown_item)
browser.execute_script("arguments[0].value = '4572'", last_dropdown_item)

dropdown = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#docsDataTable_length select"))
)
dropdown.click()

full = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#docsDataTable_length option[value='4572']"))
)
full.click()

links.extend(grab_links(browser))

print(f"Total links collected: {len(links)}")

end_time = time.time()

total_time = end_time - start_time
print(f"Total execution time: {total_time} seconds")