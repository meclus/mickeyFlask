import json
import requests


def login(baseUri):
    url = "{}/sign/in".format(baseUri)

    payload = "{\"loginName\":\"kangce\",\"password\":\"password\"}"
    headers = {'content-type': 'application/json'}
    request = requests.session()
    
    response = request.post(url, data=payload, headers=headers)
    return {
        "Cookie": response.headers['Set-Cookie'],
        "token": response.headers['token']
    }