import csv
import os
import requests
from bs4 import BeautifulSoup

def run_scraper():
    if not os.path.exists('output'):
        os.makedirs('output')
    
    print("Amazon Scraper shuru ho raha hai...")
    # Filhal basic testing ke liye
    with open('output/products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Link"])
        writer.writerow(["Test Product", "https://example.com"])
    print("Data save ho gaya.")

if __name__ == "__main__":
    run_scraper()
    
