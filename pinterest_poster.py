import os
import requests

def get_boards():
    token = os.getenv('PINTEREST_TOKEN')
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://api.pinterest.com/v5/boards", headers=headers)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    get_boards()
    
