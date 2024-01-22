import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import os

# Get book categories
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
categories = [category.text.strip() for category in soup.find('ul', class_='nav-list').find('ul').find_all('a')]

# Create an empty DataFrame to store the data
all_books_df = pd.DataFrame(columns=['Title', 'Price', 'Category', 'ImageURL'])

# Iterate through categories and extract product information
for category in categories:
    category_url = url + f'catalogue/category/books/{category.lower()}/index.html'
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting product information
    for book in soup.select('h3 a'):
        book_url = urljoin(url, 'catalogue' + book['href'][8:])
        book_response = requests.get(book_url)
        book_soup = BeautifulSoup(book_response.text, 'html.parser')
        
        title = book_soup.find('h1').text.strip()
        price = book_soup.find('p', class_='price_color').text.strip()
        image_url = urljoin(url, book_soup.find('div', class_='item active').find('img')['src'])
        
        # Download and save the image in the working directory
        image_filename = f'{title}.jpg'
        image_data = requests.get(image_url).content
        with open(image_filename, 'wb') as image_file:
            image_file.write(image_data)
        
        # Append the data to the DataFrame
        all_books_df = all_books_df.append({'Title': title, 'Price': price, 'Category': category, 'ImageURL': image_filename}, ignore_index=True)

# Write data to Excel file
excel_filename = 'all_books.xlsx'
all_books_df.to_excel(excel_filename, index=False)

print(f'Data written to {excel_filename}')
