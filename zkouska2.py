import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():

    try:
        #kontrola zda jsme se správně připojili na určitou stránku a jde s ní pracovat
        response = requests.get(url)
        if response.status_code != 200:
            return False

        #usnadnění práce s daty
        data = response.json()

        # Přidání klíče userName, pokud není userID ve slovníku, vypíše Unknown User
        for item in data:
            item['userName'] = user_names.get(item['userId'], "Unknown User")

        # Zapsání a uložení do souboru, indent přidává odszení pro čitelnost dat
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        return True
    except Exception as e:
        print(f"Došlo k chybě: {e}")
        return False

# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data), text=json.dumps(mock_data), content=json.dumps(mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test post",
                    "body": "This is a test.",
                    "userName": "Leanne Graham"
                }
            ])
