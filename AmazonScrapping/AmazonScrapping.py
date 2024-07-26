import requests
from bs4 import BeautifulSoup
from langchain_community.llms import Ollama


class ProductScraper:
    def __init__(self, item_name):
        self.item_name = item_name
        self.headers = {
            "accept-language": "en-US,en;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

    def get_product_list(self):
        url = f'https://www.amazon.in/s?k={self.item_name.replace(" ", "+")}'
        response = requests.get(url, headers=self.headers).text
        soup = BeautifulSoup(response, 'html.parser')
        products = []
        for product in soup.find_all('div', class_='s-main-slot s-result-list s-search-results sg-row'):
            for item in product.find_all('div', {'data-component-type': 's-search-result'}):
                name = item.h2.text if item.h2 else 'N/A'
                full_name = item.find('span', class_='a-size-base-plus a-color-base a-text-normal')
                avg_review = item.find('span', class_='a-size-base')
                avg_review = avg_review.text if avg_review else 'N/A'
                avg_rating = item.find('span', class_='a-icon-alt')
                avg_rating = avg_rating.text.split()[0] if avg_rating else 'N/A'
                price = item.find('span', class_='a-price-whole')
                price = price.text if price else 'N/A'
                delivery = item.find('span', class_='a-color-secondary')
                delivery = delivery.text if delivery and 'delivery' in delivery.text.lower() else 'N/A'
                link = item.find('a', {'class': 'a-link-normal'}, href=True)
                link = f"https://www.amazon.in{link['href']}" if link else 'N/A'

                products.append({
                    'Product Name': name.strip(),
                    'Full Name': full_name.text if full_name else 'N/A',
                    'Average Review': avg_review.strip(),
                    'Average Rating': avg_rating.strip(),
                    'Price': price.strip(),
                    'Delivery Time': delivery.strip(),
                    'Link': link.strip()
                })

        details_string = ""
        num = 1
        for product in products:
            details_string += f"Sl. No: {num}\n"
            details_string += f"Product Name: {product['Product Name']}\n"
            details_string += f"Full Name: {product['Full Name']}\n"
            details_string += f"Average Review: {product['Average Review']}\n"
            details_string += f"Average Rating: {product['Average Rating']}\n"
            details_string += f"Price: {product['Price']}\n"
            details_string += f"Delivery Time: {product['Delivery Time']}\n"
            details_string += f"Link: {product['Link']}\n"
            details_string += "\n"
            num += 1

        return details_string


class LLMAssistant:
    def __init__(self, model="llama3"):
        self.llm = Ollama(model=model)
        self.context = {
            "item": None,
            "dataset": None,
            "response": None
        }

    def set_item(self, item):
        self.context["item"] = item

    def set_dataset(self, dataset):
        self.context["dataset"] = dataset

    def recommend(self):
        print("LLM is processing")
        self.context['response'] = self.llm.invoke(
            f"The user has wants to buy {self.context['item']}. From the dataset given below, suggest two items that the user"
            f"should buy after reading through the ratings and price. Always try to buy something that is cheap and has better ratings and reviews. Here is the dataset \n {self.context['dataset']}"
        )
        return self.context['response']

    def follow_up_recommendation(self, question):
        print("Follow-up is processing")
        response = self.llm.invoke(
            f"The user previously asked about buying {self.context['item']}. Based on the dataset: {self.context['dataset']} and the suggestions provided: {self.context['response']}, {question}"
        )
        return response


def main(item_name=None):

    scraper = ProductScraper(item_name)
    llm_assistant = LLMAssistant()

    llm_assistant.set_item(item_name)
    dataset = scraper.get_product_list()
    llm_assistant.set_dataset(dataset)

    print(dataset)
    response = llm_assistant.recommend()
    print(response)

    while True:
        question = input("Enter any follow-up questions (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        follow_up_response = llm_assistant.follow_up_recommendation(question)
        print(follow_up_response)


if __name__ == "__main__":
    # Example on how to use it
    main(item_name= "waste basket")
