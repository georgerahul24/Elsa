# File to test scrapping of details from the goodreads page
import bs4

html = open('goodreads.html').read()

soup = bs4.BeautifulSoup(html, 'html.parser')

book_items = soup.find_all(class_="listWithDividers__item")

for book_item in book_items:
    # Extracting book name
    book_name = book_item.select_one('.gr-h3--noMargin').text.strip()

    # Extracting book summary
    book_summary = book_item.select_one('.expandableHtml').text.strip()

    # Extracting book author
    book_author = book_item.select_one('[itemprop="author"] [itemprop="name"]').text.strip()

    # Extracting book title
    book_title = book_item.select_one('[itemprop="name"]').text.strip()

    # Extracting book rating
    book_rating = book_item.select_one('.communityRating').text.strip()

    print("Book Name:", book_name)
    print("Book Summary:", book_summary)
    print("Book Author:", book_author)
    print("Book Title:", book_title)
    print("Book Rating:", book_rating)
    print()  # Add a blank line for better readability between books