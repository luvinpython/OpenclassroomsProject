# Importing modules needed for this project
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# Create a session object
session = requests.Session()

# Create a function
def sanitize_filename(filename):
    return ''.join(char for char in filename if char.isalnum() or char in [' ', '.', '_']).rstrip()

# Create another function
def download_image(image_url, filename):
    response = session.get(image_url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

# Function to scrape books from a category and creating a while loop
def scrape_books(category_url, category_name, save_folder):
    while True:
        response = session.get(category_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a['title']
            image_relative_url = book.find('img')['src']
            image_url = urljoin(url, image_relative_url)
            sanitized_title = sanitize_filename(title)
            image_filename = os.path.join(save_folder, f'{sanitized_title}.jpg')
            download_image(image_url, image_filename)
        next_page = soup.find('li', class_='next')
        if next_page:
            next_page_url = next_page.a['href']
            category_url = urljoin(category_url, next_page_url)
        else:
            break

# Get the book categories
url = 'https://books.toscrape.com/'
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
categories = soup.find('ul', class_='nav-list').find('ul').find_all('a')

# Folder to save images
save_folder = 'saved_images'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Iterate through each category and extract product images
for category in categories:
    category_name = category.text.strip()
    category_relative_url = category['href']
    category_url = urljoin(url, category_relative_url)
    scrape_books(category_url, category_name, save_folder)
    print(f'Images for {category_name} downloaded in {save_folder}')
