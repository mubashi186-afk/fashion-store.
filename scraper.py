import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_fashion_products():
    # Folder mein kya hai check karte hain
    print("Files in current directory:", os.listdir('.'))
    
    # Simple test file banate hain ye dekhne ke liye ki file write ho rahi hai ya nahi
    with open('test_file.txt', 'w') as f:
        f.write("Testing file creation")
        
    url = "https://www.amazon.com/s?k=visual+fashion"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        with open('products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Title"])
            for item in products[:10]:
                title_tag = item.find('h2')
                if title_tag:
                    writer.writerow([title_tag.text.strip()])
        print("CSV file created successfully.")
    else:
        print("Failed to access Amazon.")

if __name__ == "__main__":
    scrape_fashion_products()
    
