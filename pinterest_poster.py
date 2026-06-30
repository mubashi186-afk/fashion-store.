import os
import requests

TOKEN = os.getenv('PINTEREST_TOKEN')

def get_boards():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get("https://api.pinterest.com/v5/boards", headers=headers)
    
    print("Pinterest API Response:", response.status_code)
    print("Data:", response.json())

if __name__ == "__main__":
    get_boards()
    
