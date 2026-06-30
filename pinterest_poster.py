pinterest_poster.pyimport os
import requests
import csv

def post_to_pinterest():
    token = os.environ.get('PINTEREST_TOKEN')
    
    # CSV file se data padhna
    with open('output/products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row['Product Title']
            link = row['Link']
            
            # Pinterest API call
            url = "https://api.pinterest.com/v5/pins"
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            data = {
                "link": link,
                "title": title,
                "description": f"Check out this amazing fashion item: {title}",
                "media_source": {"source_type": "image_url", "url": "https://via.placeholder.com/150"}
            }
            
            response = requests.post(url, json=data, headers=headers)
            print(f"Pin Status: {response.status_code}")

if __name__ == "__main__":
    post_to_pinterest()
  
