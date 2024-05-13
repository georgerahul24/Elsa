import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()  # Change this to the appropriate WebDriver for your browser

# Load the webpage
driver.get("https://www.goodreads.com/book/similar/3346751-percy-jackson-and-the-lightning-thief")

# Wait for the "More" button to become clickable
buttons = driver.find_elements(By.CSS_SELECTOR, ".gr-buttonAsLink.u-marginLeftTiny")

# Click buttons one by one until none are found (or another condition)
for button in buttons:
    try:
        button.click()

    except NoSuchElementException:
        # No more buttons found, break the loop
        break
soup = BeautifulSoup.BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Now you can continue parsing and extracting information from the updated HTML content using BeautifulSoup
book_items = soup.find_all(class_="listWithDividers__item")

for book_item in book_items:
    # Extracting book name
    book_name = book_item.select_one('.gr-h3--noMargin').text.strip()

    # Extracting book summary
    book_summary = book_item.select_one('.expandableHtml').text.strip()

    # Extracting book author
    book_author = book_item.select_one('[itemprop="author"] [itemprop="name"]').text.strip()

    # Extracting book rating
    book_rating = book_item.select_one('.communityRating').text.strip()

    print("Book Name:", book_name)
    print("Book Summary:", book_summary)
    print("Book Author:", book_author)
    print("Book Rating:", book_rating)
    print()  # Add a blank line for better readability between books
