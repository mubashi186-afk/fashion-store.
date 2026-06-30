import csv
import os
import requests
from bs4 import BeautifulSoup

# Tumhari Affiliate ID yahan fix hai
TAG = "mubashirsto0b-20"

def get_affiliate_link(link):
    # Link ke peeche tumhari ID jodna
    if "?" in link:
        return f"{link}&tag={TAG}"
    else:
        return f"{link}?tag={TAG}"

def scrape_fashion_products():
    # Folder banana
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Amazon search URL
    url = "https://www.amazon.com/s?k=mens+fashion"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    
    print("Agent shuru ho raha hai...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        # File mein save karna
        with open('output/products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Link", "Image"])
            
            count = 0
            for item in products:
                if count >= 10: break
                
                title_tag = item.find('h2')
                link_tag = item.find('a', {'class': 'a-link-normal'})
                img_tag = item.find('img', {'class': 's-image'})
                
                if title_tag and link_tag and img_tag:
                    title = title_tag.text.strip()
                    # Link ko Amazon domain ke sath pura karna
                    raw_link = "https://www.amazon.com" + link_tag['href']
                    # Affiliate link banana
                    affiliate_link = get_affiliate_link(raw_link)
                    img = img_tag['src']
                    
                    writer.writerow([title, affiliate_link, img])
                    count += 1
        print(f"Success: {count} Products scrape ho gaye aur file save ho gayi!")
    else:
        print(f"Error: Amazon ne block kiya, Status Code: {response.status_code}")

if __name__ == "__main__":
    scrape_fashion_products()
    
