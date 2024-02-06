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