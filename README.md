# Python Book Inventory Application
Below is the info on how to run the Python application for the Price Monitoring System Project from the website: 

https://books.toscrape.com/

The project does require a basic understanding of the Python programming language and more info for Python can be found at:

https://www.python.org/

## The Program
This application pulls various needed data from the website and organizes it into categories to be exported to a CSV file for the user.
It organizes these pieces of data into multiple excel files. The reason for this program is it makes viewing pieces of data much easier for the user. 
It saves users time and can be sent in emails or as attachments to many users giving info across the website.
This project can be adapted in the future to scrape a number of different websites and pull multiple pieces of info


### Setting up the IDE (optional):
1. Go to https://www.jetbrains.com/pycharm/
   and download the program for your given operating system. 
    Or to https://code.visualstudio.com/
   to use VS Code if you prefer
3. Download python
   from https://www.python.org/downloads/ version 3.12.1 or higher for your specific operating system. 
5. Open it and create a new project
6. Download the code
7. Extract the code to preferred location
8. In the IDE go to file open and navigate to the location you extracted the code from and select the main.py
(optional) Navigate the the extracted folder location and double click the main.py file and it will run automtically in the terminal

### Instructions for Terminal (Windows):
1. Download files from this repository or create a clone using the code below.

    $ git clone https://github.com/luvinpython/OpenclassroomsProject

2. Navigate to the directory containing the repository.

    $ cd books_online_phase1.py

3. Using these terminal commands, create and activate a virtual environment.

    $ python -m venv env

    $ env/scripts/activate (this step may be required for some)

5. Use the command below to install the packages according to the configuration file requirements.txt.

    $ pip install -r requirements.txt

6. Open and run the file allcategories.py to download product data in CSV format and product images.

    $ .\main.py

### Instructions for Mac:

1. Download files from this repository or create a clone using the code below.

   $ git clone https://github.com/luvinpython/OpenclassroomsProject

2. Navigate to the directory containing the repository.

    $ cd books_online_phase1.py

3. Using these terminal commands, create and activate a virtual environment.

    $ python -m venv env

    $ source env/bin/activate

4. Use the command below to install the packages according to the configuration file requirements.txt.

    $ python3 -m pip install -r requirements.txt

5. Open and run the file allcategories.py to download product data in CSV format and product images.

    $ python main.py
