import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_fashion_products():
    if not os.path.exists('output'):
        os.makedirs('output')
        
    url = "https://www.amazon.com/s?k=fashion"
    # Ye headers asli browser jaisa behave karenge
    headers = {
        "User-Agent": "Mozilla/5.0 (Android 10; Mobile; rv:86.0) Gecko/86.0 Firefox/86.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}") # Ye humein batayega ki Amazon allow kar raha hai ya nahi
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        with open('output/products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Title"])
            for item in products:
                title_tag = item.find('h2')
                if title_tag:
                    writer.writerow([title_tag.text.strip()])
        print("Data scrape ho gaya!")
    else:
        print("Amazon ne block kar diya!")

if __name__ == "__main__":
    scrape_fashion_products()
                  
