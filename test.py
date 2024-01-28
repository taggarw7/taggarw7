import requests
# Trello API key and token (replace with your own)
API_KEY = "879be7235a1c8f6543aaeac39666699e"
TOKEN = "ATTA915988ab2f97f6fd1a81a5c9d23afe7803feb3272d5c5c743928ccc83a82eb154A54657C"

# Trello board ID and column name (replace with your own)
BOARD_ID = "65b5a4ea445dc2a9f22e6de7"
COLUMN_NAME = "To Do"

#checking if api key and token are valid or no
def check_api_key_and_token():
    url = f"https://api.trello.com/1/members/me"
    params = {
        'key': API_KEY,
        'token': TOKEN,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("API key and token are valid.")
    else:
        print("Failed to authenticate. Status code:", response.status_code)
        print(response.text)
  
#Checking if the boardid is valid or not       
def is_valid_board_id(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}"
    params = {
        'key': API_KEY,
        'token': TOKEN,
    }
    response = requests.get(url, params=params)
    return response.status_code == 200

#getting corresponding id for the column name(TO DO)
def get_list_id(board_id, list_name):
    if not is_valid_board_id(board_id):
        print(f"Invalid board ID: {board_id}")
        return None
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    params = {
        'key': API_KEY,
        'token': TOKEN,
    }
    response = requests.get(url, params=params)
    lists = response.json()
    #print(lists)
    for lst in lists:
        if lst['name'] == list_name:
            return lst['id']
    print(f"List '{list_name}' not found on the board.")
    return None

#creating new card with comment and label
def create_card(list_id, name, labels=None, comment=None):
    url = f"https://api.trello.com/1/cards"
    params = {
        'key': API_KEY,
        'token': TOKEN,
        'idList': list_id,
        'name': name,
        'desc': comment,
        'idLabels': labels,
    }

    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Card created successfully.")
    else:
        print(f"Failed to create card. Status code: {response.status_code}")
        print(response.text)



if __name__ == "__main__":
    card_name = input("Enter the card name: ")
    labels = input("Enter labels").split(',')
    comment = input("Enter a comment for the card: ")
    list_id = get_list_id(BOARD_ID, COLUMN_NAME)
    if list_id:
        create_card(list_id, card_name, labels, comment)