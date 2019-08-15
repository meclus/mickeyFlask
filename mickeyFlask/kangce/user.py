import json
import requests


def login(baseUri, isdebug):

    if isdebug:
        # "http://192.168.31.144:8100"
        baseUri = "http://127.0.0.1:8100"

    url = "{}/sign/in".format(baseUri)

    payload = "{\"loginName\":\"kangce005\",\"password\":\"password\"}"
    headers = {'content-type': 'application/json'}
    request = requests.session()
    response = request.post(url, data=payload, headers=headers)
    print(response.text)
    return {
        "content-type": 'application/json',
        "token": response.headers['token']
    }