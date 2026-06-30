import csv
import requests
from bs4 import BeautifulSoup

def scrape_fashion_products():
    # Hum dummy "fashion" ki jagah seedha URL use karenge aur headers ko aur strong karenge
    url = "https://www.amazon.com/s?k=mens+fashion"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    # Agar code 200 hai to data process karo
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        with open('output/products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Title"])
            for item in products:
                # Sirf title nahi, price aur link bhi uthane ki koshish karenge
                title = item.find('h2')
                if title:
                    writer.writerow([title.text.strip()])
        print("Data scrape ho gaya!")
    else:
        # Agar code 200 nahi hai, to error print karo
        print(f"Error: Amazon ne block kiya, Status Code: {response.status_code}")

if __name__ == "__main__":
    scrape_fashion_products()
            
