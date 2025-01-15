import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape Amazon
def scrape_amazon(query):
    amazon_url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(amazon_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    for item in soup.find_all('div', {'class': 's-main-slot'}):
        titles = item.find_all('span', {'class': 'a-text-normal'})
        prices = item.find_all('span', {'class': 'a-price-whole'})
        ratings = item.find_all('span', {'class': 'a-icon-alt'})
        
        for title, price, rating in zip(titles, prices, ratings):
            product_name = title.text.strip()
            product_price = price.text.strip() if price else 'N/A'
            product_rating = rating.text.strip() if rating else 'N/A'
            
            products.append([product_name, product_price, product_rating])

    return products

# Function to scrape Flipkart
def scrape_flipkart(query):
    flipkart_url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(flipkart_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    for item in soup.find_all('div', {'class': '_1AtVbE'}):
        titles = item.find_all('a', {'class': 'IRpwTa'})
        prices = item.find_all('div', {'class': '_30jeq3'})
        ratings = item.find_all('div', {'class': '_3LWZlK'})
        
        for title, price, rating in zip(titles, prices, ratings):
            product_name = title.text.strip() if title else 'N/A'
            product_price = price.text.strip() if price else 'N/A'
            product_rating = rating.text.strip() if rating else 'N/A'
            
            products.append([product_name, product_price, product_rating])

    return products

# Main Function
def main():
    query = input("Enter the product you want to search for: ")
    
    amazon_products = scrape_amazon(query)
    flipkart_products = scrape_flipkart(query)

    # Combine data from both sources
    all_products = amazon_products + flipkart_products
    
    # Save the product details to an Excel file
    df = pd.DataFrame(all_products, columns=['Product Name', 'Price', 'Rating'])
    df.to_excel(f"{query}_products.xlsx", index=False, engine='openpyxl')
    print(f"Product details saved in {query}_products.xlsx")

# Run the script
if __name__ == "__main__":
    main()
