import requests

base_url = "http://127.0.0.1:8000/api/"

login_url = base_url + "auth/token/"

projects_url = base_url + "products/"

refresh_url = login_url + "refresh/"

data = {
    "username": "awesomepants",
    "password": "pantsawesome",
}

login_r = requests.post(login_url, data=data)

import json

json.dumps(json_data, indent=2)

token= json_data["token"]

headers = {
    "Authorization": "JWT %s" %s(token),
}

p_r = requests.get(products_url, headers=headers)

data = {
    "token": token,
}
refresh_r = requests.post(refresh_url, data=data)

token = refresh_r.json()["token"]
