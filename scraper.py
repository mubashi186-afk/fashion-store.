import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_fashion_products():
    # Folder banana
    if not os.path.exists('output'):
        os.makedirs('output')
        
    url = "https://www.amazon.com/s?k=visual+fashion"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        # File path "output/products.csv"
        with open('output/products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Title"])
            for item in products[:10]:
                title_tag = item.find('h2')
                if title_tag:
                    writer.writerow([title_tag.text.strip()])
        print("File saved in output folder.")

if __name__ == "__main__":
    scrape_fashion_products()
    
