import os
import requests

TOKEN = os.getenv('PINTEREST_TOKEN')

def get_board_id():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    # Tumhare account ke boards ki list mang rahe hain
    response = requests.get("https://api.pinterest.com/v5/boards", headers=headers)
    
    if response.status_code == 200:
        boards = response.json().get('items', [])
        for board in boards:
            print(f"Board Name: {board['name']} | Board ID: {board['id']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    get_board_id()
    
