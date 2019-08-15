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
    print(url)
    response = requests.get(url, headers=login_response)
    util.file.write(json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False), "schema.json")
    #print(response.json())
    for item in response.json()['data']:
        field_settings = dict((field['fieldsName'], field['nameChs']) for field in item['fieldDisplayDtos'])
        for field in item['fieldDisplayDtos']:
            for sub_dis in field['subsidiaryFieldDtos']:
                # print(sub_dis['fieldsname'] in field_settings.keys())
                if sub_dis['fieldsname'] not in field_settings.keys():
                    print(sub_dis['fieldsname'])
