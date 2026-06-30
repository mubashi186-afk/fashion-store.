import csv
import os
import requests
from bs4 import BeautifulSoup

# Tumhari Affiliate ID
TAG = "mubashirsto0b-20"

def get_affiliate_link(link):
    if "?" in link:
        return f"{link}&tag={TAG}"
    else:
        return f"{link}?tag={TAG}"

def run_scraper():
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Fashion items ke liye Amazon Search URL
    url = "https://www.amazon.com/s?k=mens+fashion"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    
    print("Amazon se real products utha raha hoon...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        with open('output/products.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Link"])
            
            count = 0
            for item in products:
                if count >= 10: break
                title_tag = item.find('h2')
                link_tag = item.find('a', {'class': 'a-link-normal'})
                
                if title_tag and link_tag:
                    title = title_tag.text.strip()
                    raw_link = "https://www.amazon.com" + link_tag['href']
                    writer.writerow([title, get_affiliate_link(raw_link)])
                    count += 1
        print(f"{count} Products successfully save ho gaye!")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    run_scraper()
            
