This repository contains the work I've done for my OpenClassrooms project for "Use Python Basics for Market Analysis". It's designed to showcase my skills and knowledge gained through the OpenClassroom course. I am comfortable using Python and can use it to develop a web scrapping tool. It demonstrates the application of Python, beautiful soup, requests and the pandas libraries. I have the code included for each phase below and it is also in my GitHub repository. I have included comments below on the code and a quick summary on each phase of what I have written for the Price Monitoring System.

Phase 1

This code imports the modules listed below to help extract the data on the single product page just for the book "Gone with the Wind". I have the website in a variable and then print the status code to show the webpage is up and running properly.

I then create a soup object using html parser and use the html tags to create headers to use in the pandas data frame.

The pandas data frame then formats the data correctly and uploads to a CSV file. Unfortunately I couldn't remove the odd symbol by the pound symbol. 


# Importing modules the needed for this project, added pandas modules
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Store the website url of Gone with the Wind book in a variable
website = "https://books.toscrape.com/catalogue/gone-with-the-wind_324/index.html"

# Get Request and Status Code to see if website is active 
response = requests.get(website)
print(response.status_code)

# Create a Soup Object using the html parser
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting each piece of data from the website 
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

# Create a DataFrame using pandas module
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

# use pandas library to create dataframe as it formats data correctly
df = pd.DataFrame(data)

# Write the info to a CSV file titled Gone_with_the_Wind
df.to_csv('Gone_with _the_Wind.csv', index=False)










Phase 2 

Similar to the code previously but this code extracts the travel books category and shows all 11 books just in that particular category. 

Like before I have the website in a variable and then print the status code to show the webpage is up and running properly.

I then create a soup object using html parser and use the html tags to create headers to use in the pandas data frame.

As before the pandas data frame then formats the data correctly and uploads to a CSV file. 

Unfortunately I still couldn't remove the odd symbol by the pound symbol. 




# Importing modules the needed for this project, added pandas modules
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Store the website url of Gone with the Wind book in a variable
website = "https://books.toscrape.com/catalogue/gone-with-the-wind_324/index.html"

# Get Request and Status Code to see if website is active 
response = requests.get(website)
print(response.status_code)

# Create a Soup Object using the html parser
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting each piece of data from the website 
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

# Create a DataFrame using pandas module
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

# use pandas library to create dataframe as it formats data correctly
df = pd.DataFrame(data)

# Write the info to a CSV file titled Gone_with_the_Wind
df.to_csv('Gone_with _the_Wind.csv', index=False)



Phase 3

Similar to the code previously but this code extracts all 52 book categories and shows all books in a seperate CSV file by category. 

I created a funtion and a while loop inside starting with an empty list and then appending the new data file from each category. Once the loop ends it breaks and the data is complete. 

Unfortunately I still couldn't remove the odd symbol by the pound symbol. 





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






Phase 4


Similar to the previous phases this code pulls all images and is quite lengthly. It has each in a seperate png file for over 1000 images on the site. 

For this I also used url lib and os modules.

Once again I created a funtion and a while loop inside starting with an empty list and then appending the new data file from each category.






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

