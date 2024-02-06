# Importing modules needed for this project
import requests
from bs4 import BeautifulSoup
import csv

# Create a session object
session = requests.Session()

# Function to scrape books from a category and create while loop starting with empty loop
def scrape_books(category_url, category_name):
    books = []
    while True:
        response = session.get(category_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            # Add more details as needed
            books.append({'Title': title, 'Price': price, 'Category': category_name})
        next_page = soup.find('li', class_='next')
        if next_page:
            category_url = url + next_page.a['href']
        else:
            break
    return books

# Get the book categories
url = 'https://books.toscrape.com/'
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
categories = soup.find('ul', class_='nav-list').find('ul').find_all('a')

# Iterate through each category and extract product information
for category in categories:
    category_name = category.text.strip()
    category_relative_url = category['href']
    category_url = url + category_relative_url
    books = scrape_books(category_url, category_name)
    
    # Write data to CSV file
    filename = f'{category_name}_books.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Price', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow(book)
    
    print(f'Data for {category_name} written to {filename}')
