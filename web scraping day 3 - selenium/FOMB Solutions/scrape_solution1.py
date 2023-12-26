from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

start_time = time.time() 


def grab_links(browser):
    links = []

    rows = browser.find_elements(By.CSS_SELECTOR, "#docsDataTable tbody tr")
    for row in rows:
        link_element = row.find_element(By.TAG_NAME, 'a')
        href_value = link_element.get_attribute('href')
        links.append(href_value)

    return links

# Start the webdriver
browser = webdriver.Firefox()
browser.get('https://juntasupervision.pr.gov/documents/')

try:
    # Set display to 100 rows per page
    dropdown = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#docsDataTable_length select"))
    )
    dropdown.click()

    option_100 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#docsDataTable_length option[value='100']"))
    )
    option_100.click()

    links = []

    # Get the last pagination link's text to determine the final page
    last_page_element = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.paginate_button:nth-child(7)"))
    )
    last_page = int(last_page_element.text) if last_page_element.text else 1

    # Loop through pages
    for _ in range(1, last_page + 1):
        links.extend(grab_links(browser))
        try:
            next_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.ID, "docsDataTable_next"))
            )
            next_button.click()
            time.sleep(2)  # Adding a delay for the page to load
        except Exception as e:
            print(f"Error clicking next button: {str(e)}")
            break

    print(f"Total links collected: {len(links)}")
    for link in links:
        print(link)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total execution time: {total_time} seconds")
    

except Exception as e:
    print(f"An error occurred: {str(e)}")

