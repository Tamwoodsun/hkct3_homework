# Homework to automatic gen web page of "European Champion League" fromm google.com
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome() 

try:
    # Visit Google.com
    driver.get("https://www.google.com")

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")

    # Input the search query
    search_box.send_keys("European Champion League")
    search_box.submit()  # Submit the search

    # Wait for the results page to load and display the results
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3")))

    # Click the first link in the search results
    first_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h3"))
    )
    first_link.click()

    # Optional: Wait for the new page to load completely, if needed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

finally:
    
    
    driver.quit()