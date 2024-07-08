import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_product_list(url):
    headers = {"accept-language": "en-US,en;q=0.9", "accept-encoding": "gzip, deflate, br",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
               "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

    response = requests.get(url, headers=headers).text


    soup = BeautifulSoup(response, 'html.parser')

    # Extract product details including price and correct delivery time
    products = []
    for product in soup.find_all('div', class_='s-main-slot s-result-list s-search-results sg-row'):
        for item in product.find_all('div', {'data-component-type': 's-search-result'}):
            name = item.h2.text if item.h2 else 'N/A'
            avg_review = item.find('span', class_='a-size-base')
            avg_review = avg_review.text if avg_review else 'N/A'
            avg_rating = item.find('span', class_='a-icon-alt')
            avg_rating = avg_rating.text.split()[0] if avg_rating else 'N/A'
            price = item.find('span', class_='a-price-whole')
            price = price.text if price else 'N/A'
            delivery = item.find('span', class_='a-color-secondary')
            delivery = delivery.text if delivery and 'delivery' in delivery.text.lower() else 'N/A'

            products.append({
                'Product Name': name.strip(),
                'Average Review': avg_review.strip(),
                'Average Rating': avg_rating.strip(),
                'Price': price.strip(),
                'Delivery Time': delivery.strip()
            })

    details_string = ""
    for product in products:
                details_string += f"Product Name: {product['Product Name']}\n"
                details_string += f"Average Review: {product['Average Review']}\n"
                details_string += f"Average Rating: {product['Average Rating']}\n"
                details_string += f"Price: {product['Price']}\n"
                details_string += f"Delivery Time: {product['Delivery Time']}\n"
                details_string += "\n"
    return details_string

print(get_product_list('https://www.amazon.in/s?k=macbook+pro'))
