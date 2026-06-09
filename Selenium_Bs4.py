"""
Google Search Scraper Project
-----------------------------
This project automates a Google search using Selenium WebDriver.
It retrieves the search results page, parses the HTML content
using BeautifulSoup (BS4), extracts result titles (h3 tags),
and appends them to a local text file.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Initialize Chrome Service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Locate search bar and perform search
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("آموزش پایتون مکتبخونه")
    search_bar.send_keys(Keys.ENTER)

    # Wait for results to load fully
    time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract all result titles (h3 elements)
    name_list = soup.find_all("h3")

    # Save the extracted data to names.txt
    with open("names.txt", "a", encoding="utf-8") as f:
        for name in name_list:
            # Using .get_text() or .text to extract the string
            f.write(name.get_text() + "\n")

    print(f"Operation complete: {len(name_list)} items saved.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Ensure the browser closes properly
    driver.quit()
