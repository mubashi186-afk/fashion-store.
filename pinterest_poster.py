import os
import requests
import json

TOKEN = os.getenv('PINTEREST_TOKEN')

def get_boards():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get("https://api.pinterest.com/v5/boards", headers=headers)
    
    # Ye tumhare boards ki list ek file mein save kar dega
    with open('boards.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
    print("Boards ki list 'boards.json' file mein save ho gayi hai!")

if __name__ == "__main__":
    get_boards()
    
