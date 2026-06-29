import requests
from bs4 import BeautifulSoup

def scrape_fashion_products():
    # Ye target URL hai jahan se hum visual fashion products uthayenge
    url = "https://www.amazon.com/s?k=visual+fashion"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Products ki list dhoondna
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    for item in products[:10]: # Sirf 10 products
        title = item.find('h2').text.strip()
        print(f"Scraped Product: {title}")

if __name__ == "__main__":
    scrape_fashion_products()
      
