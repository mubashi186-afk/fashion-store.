import requests
from bs4 import BeautifulSoup

def scrape_fashion_products():
    # Amazon search URL
    url = "https://www.amazon.com/s?k=visual+fashion"
    
    # Ye headers bot nahi lagne denge
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        print(f"Total products found: {len(products)}")
        
        for item in products[:10]:
            try:
                title_tag = item.find('h2')
                if title_tag:
                    print(f"Scraped Product: {title_tag.text.strip()}")
            except Exception as e:
                continue
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_fashion_products()
                        
