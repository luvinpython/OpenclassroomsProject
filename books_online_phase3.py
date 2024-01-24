# Importing modules
import requests
from bs4 import BeautifulSoup
import csv

# Get the book categories
url = 'https://books.toscrape.com/'
response = requests.get(url)
# Create a Soup Object using the html parser
soup = BeautifulSoup(response.text, 'html.parser')
categories = [category.text.strip() for category in soup.find('ul', class_='nav-list').find('ul').find_all('a')]

# Iterate through each category and extract product information
for category in categories:
    category_url = url + f'catalogue/category/books/{category.lower()}/index.html'
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting product information start with an empty lsit 
    books = []
    for book in soup.find_all('h3'):
        title = book.a['title']
        price = book.find('p', class_='price_color').text
        books.append({'Title': title, 'Price': price, 'Category': category})
    
    # Write data to CSV file
    filename = f'{category}_books.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Price', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
        
    # Has all categories in seperate CSV files but not the info
    print(f'Data for {category} written to {filename}')
