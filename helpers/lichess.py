import json

import requests

# Documentation can be found in https://lichess.org/api#tag/Challenges/operation/challengeAi
url = 'https://lichess.org/api/challenge/open'


def get_lichess_link():
    req = requests.post(url, json=None)
    content = json.loads(req.text)
    return content["challenge"]["url"]
