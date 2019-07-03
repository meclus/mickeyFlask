# encoding:utf-8

import json
import requests

import util.file


def clean_redis(baseuri, login_response, companyid):
    url = "{}/baseinfo/public/cleanCompanyRedisCache/{}".format(baseuri, companyid)
    print(url)
    resp = requests.get(url, headers=login_response)
    print(resp.text)


def get_schema4add(pvbaseuri, login_response):
    url = "{}/icsr/schema/report/add".format(pvbaseuri)
    response = requests.get(url, headers=login_response)
    util.file.write(json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False), "add_schema.json")


def get_schema(pvbaseuri, login_response):
    url = "{}/icsr/schema/report".format(pvbaseuri)
    response = requests.get(url, headers=login_response)
    util.file.write(json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False), "schema.json")
    for item in response.json()['data']:
        for field in item['fieldDisplayDtos']:
            print('{}       {}'.format(field['fieldsName'], field['nameChs']))
    
def print_json(json):
    print(json.dumps(json, sort_keys=True, indent=4, ensure_ascii=False))