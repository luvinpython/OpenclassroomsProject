# Importing modules 
import requests
from bs4 import BeautifulSoup
import pandas as pd

def process_single_book(website):
    # Get Request and Status Code
    response = requests.get(website, verify=True)

    # Create a Soup Object. Use html parser
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting information
    product_page_url = website
    universal_product_code = soup.find('th', string='UPC').find_next('td').get_text()
    book_title = soup.find('h1').get_text()
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').get_text()
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').get_text()
    quantity_available = soup.find('th', string='Availability').find_next('td').get_text()
    product_description = soup.find('meta', {'name': 'description'})['content']
    category_element = soup.find('a', {'href': '../category/books/index.html'})
    category = category_element.find_next('a').get_text() if category_element else None
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('img')['src']

    # Create a DataFrame
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
    return pd.DataFrame(data)

# Store the website and travel category in a variable
base_url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
all_books_data = pd.DataFrame()

# Create a while loop
while True:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    book_links = soup.select('.product_pod h3 a')

    # Create a for loop and loop through each book link
    for link in book_links:
        # Create the full book URL
        book_url = f"https://books.toscrape.com/catalogue{link['href'][8:]}"
        book_data = process_single_book(book_url)
        all_books_data = pd.concat([all_books_data, book_data], ignore_index=True)

    # Check if there is a "Next" button on the page
    next_button = soup.select_one('.next a')
    if next_button:
        # Update the base URL to the next page
        base_url = f"https://books.toscrape.com/catalogue/category/books/travel_2/{next_button['href']}"
        print(f"Updating base_url to: {base_url}")
    else:
        # Stop the loop if there is no "Next" button
        break

# Write all info from just the TRAVEL books category to the CSV file
all_books_data.to_csv('travel_books_category.csv', index=False)
