import os
import requests

TOKEN = os.getenv('PINTEREST_TOKEN')

def get_boards():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get("https://api.pinterest.com/v5/boards", headers=headers)
    
    if response.status_code == 200:
        boards = response.json().get('items', [])
        for board in boards:
            print(f"Board Name: {board['name']} | Board ID: {board['id']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_boards()
    
