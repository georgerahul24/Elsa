import requests
from bs4 import BeautifulSoup


def get_product_list(url):
    headers = {"accept-language": "en-US,en;q=0.9", "accept-encoding": "gzip, deflate, br",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
               "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

    response = requests.get(url, headers=headers).text

    soup = BeautifulSoup(response, 'html.parser')

    # Extract product name
    product_name = soup.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2').find(
        'a').text.strip()

    # Extract review information (may not be available)

    # Extract current price
    price_container = soup.find('span', class_='a-offscreen')
    current_price = price_container.text.strip() if price_container else None

    # Extract delivery options
    delivery_options = []
    delivery_info_container = soup.find('div', id='deliveryMessageInner')
    if delivery_info_container:
        for bullet_point in delivery_info_container.find_all('li'):
            delivery_options.append(bullet_point.text.strip())

    return {
        'name': product_name,
        'average_rating': average_rating_str,
        'current_price': current_price,
        'delivery_options': delivery_options
    }


print(get_product_list('https://www.amazon.in/s?k=macbook+pro'))
