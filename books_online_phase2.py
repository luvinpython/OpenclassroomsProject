import requests
from bs4 import BeautifulSoup
import pandas as pd

# Main scraping logic
base_url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
all_books_data = pd.DataFrame()

while True:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    book_links = soup.select('.product_pod h3 a')

    for link in book_links:
        book_url = f"https://books.toscrape.com/catalogue{link['href'][8:]}"
        response = requests.get(book_url)
        book_soup = BeautifulSoup(response.content, 'html.parser')

        product_page_url = book_url
        universal_product_code = book_soup.find('th', string='UPC').find_next('td').get_text()
        book_title = book_soup.find('h1').get_text()
        price_including_tax = book_soup.find('th', string='Price (incl. tax)').find_next('td').get_text().replace('Â', '').encode('utf-8').decode('utf-8')
        price_excluding_tax = book_soup.find('th', string='Price (excl. tax)').find_next('td').get_text().replace('Â', '').encode('utf-8').decode('utf-8')
        quantity_available = book_soup.find('th', string='Availability').find_next('td').get_text()
        product_description = book_soup.find('meta', {'name': 'description'})['content']
        category_element = book_soup.find('a', {'href': '../category/books/index.html'})
        category = category_element.find_next('a').get_text() if category_element else None
        review_rating = book_soup.find('p', class_='star-rating')['class'][1]
        image_url = book_soup.find('img')['src']

        data = {
            'product_page_url': [product_page_url],
            'universal_product_code (upc)': [universal_product_code],
            'book_title': [book_title],
            'price_including_tax': [price_including_tax],
            'price_excluding_tax': [price_excluding_tax],
            'quantity_available': [quantity_available],
            'product_description': [product_description],
            'category': [category],
            'review_rating': [review_rating],
            'image_url': [image_url],
        }

        book_data = pd.DataFrame(data)
        all_books_data = pd.concat([all_books_data, book_data], ignore_index=True)

    next_button = soup.select_one('.next a')
    if next_button:
        base_url = f"https://books.toscrape.com/catalogue/category/books/travel_2/{next_button['href']}"
        print(f"Updating base_url to: {base_url}")
    else:
        break

# Write to CSV
all_books_data.to_csv('travel_books_info.csv', index=False)
