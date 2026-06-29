import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_fashion_products():
    url = "https://www.amazon.com/s?k=visual+fashion"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        # Sahi path par file save karna
        file_path = os.path.join(os.getcwd(), 'products.csv')
        
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Title"]) 
            
            for item in products[:10]:
                title_tag = item.find('h2')
                if title_tag:
                    title = title_tag.text.strip()
                    writer.writerow([title])
                    print(f"Saved: {title}")
        print(f"Data successfully saved to {file_path}")
    else:
        print("Failed to fetch page.")

if __name__ == "__main__":
    scrape_fashion_products()
                
