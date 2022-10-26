import os

import requests
import json

from dotenv import dotenv_values, load_dotenv

load_dotenv()
url = 'https://api.jsonbin.io/v3/b/635968a72b3499323beb7dee?meta=false'
headers = {
    'X-Master-Key': os.getenv('JSON_KEY'),
}


# req = requests.get(url, json=None, headers=headers)
# json_txt:dict = json.loads(req.text)
# json_txt.pop("metadata")
# counter = json_txt["record"]["counter"]
# print(counter)


def update_counter():
    req = requests.get(url, json=None, headers=headers)
    counter = json.loads(req.text)["counter"]
    counter += 1
    update_json = {"counter": counter}
    req = requests.put(url, json=update_json, headers=headers)
    json_txt = json.loads(req.text)
    counter = json_txt["record"]["counter"]
    return counter

def reset_counter():
    update_json = {"counter": 0}
    requests.put(url, json=update_json, headers=headers)
    print("The counter has been reset")

reset_counter()