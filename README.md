# Web-Scraping
This code allows you to scrape product details such as such as name, price, and ratings from two e-commerce websites 
like Amazon and Flipkart. After scraping the data, it saves the results to an Excel file.

first we install  necessary Python libraries:
requests: Used to send HTTP requests to web pages.
BeautifulSoup from bs4: Used for parsing and extracting data from HTML documents.
pip install requests beautifulsoup4 pandas openpyxl
pandas: Used to organize the scraped data and save it to an Excel file.
pip install pandas
openpyxl: Required by pandas to write to Excel files.

Define function to scrap data from amazon
create amazon search URL also the Flipcart
get request using requests library
HTML response using BeautifulSoup.

Extract product data: Using BeautifulSoup's find_all() method,
we search for the HTML elements that contain product details such as name, price, and rating.
Sending GET requests to Amazon and Flipkart.
Parsing HTML content with BeautifulSoup to extract product details.
Storing data in a list and saving it to an Excel file using pandas 
Store the scraped data: For each product, we store the name, price, and rating in a list
