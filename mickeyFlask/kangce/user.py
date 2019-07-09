import json
import requests


def login(baseUri, isdebug):

    if isdebug:
        baseUri = "http://192.168.31.144:8100"

    url = "{}/sign/in".format(baseUri)

    payload = "{\"loginName\":\"kangce\",\"password\":\"password\"}"
    headers = {'content-type': 'application/json'}
    request = requests.session()
    response = request.post(url, data=payload, headers=headers)
    return {
        "content-type": 'application/json',
        "Cookie": response.headers['Set-Cookie'],
        "token": response.headers['token']
    }