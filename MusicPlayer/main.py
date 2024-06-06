import time

import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# TODO: Error when using the headless mode. Make this headless since it would be better
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://open.spotify.com/search/armaan%20malik")

with open("yt.html", "w") as f:
    f.write(driver.page_source)

