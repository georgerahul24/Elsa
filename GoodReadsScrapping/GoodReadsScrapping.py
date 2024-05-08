import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
headers = {"accept-language": "en-US,en;q=0.9", "accept-encoding": "gzip, deflate, br",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
           "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}



def readGoodReadsSimilarPage(booklink):
   response = requests.get(booklink, headers=headers)
   print(response.text)

def searchGoogleForGoodBooksLinks(bookName):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Create a new headless Chrome session
    driver = webdriver.Chrome(options=options)

    # Construct the Google Search URL
    search_url = f"https://www.google.com/search?q={'+'.join(bookName.split())}"

    # Open the search URL in the browser
    driver.get(search_url)

    # Wait for the search results to load (adjust timeout as needed)
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "main")))
    except TimeoutException:
        print("Search results failed to load the google results page.")
        return None

    # Get the HTML content of the page
    html_content = driver.page_source
    # Close the browser window


    similarLink = re.findall(r'href="(https://www.goodreads.com/book/similar/[^"]+)"', html_content)[0]
    print("Link:", similarLink)
    driver.quit()


    return readGoodReadsSimilarPage(similarLink)









searchGoogleForGoodBooksLinks('books like Lightning Thief')