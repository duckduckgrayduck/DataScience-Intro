from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Initialize the Firefox driver
driver = webdriver.Firefox()

# Navigate to the URL
url = "https://the-internet.herokuapp.com/infinite_scroll"
driver.get(url)

# Set a timeout for the WebDriverWait
wait = WebDriverWait(driver, 10)
flag = 0 # First page content has 2 elements, not 1. 
try:
    while True:
        # Get the initial count of elements with class "jscroll-added"
        initial_element_count = len(driver.find_elements(By.CLASS_NAME, 'jscroll-added'))

        # Scroll down
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

        # Wait for new elements to appear
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'jscroll-loading')))

        # Get the first elements on the page, then only the last new element (the new paragraph)
        new_elements = driver.find_elements(By.CLASS_NAME, 'jscroll-added')

        if flag == 0:
            # Print the content of new elements
            for element in new_elements:
                print(element.text)
            flag = 1
        else:
            last_element = new_elements[-1]
            print(last_element.text)

        # Check if no new content is loaded
        if len(new_elements) == initial_element_count:
            break
        time.sleep(10)

except KeyboardInterrupt:
    # Handle the KeyboardInterrupt to close the browser on manual interruption
    time.sleep(200)
