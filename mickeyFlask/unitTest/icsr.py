import requests
import json
import util.tool


def search_icsr(pvbaseuri, login_response):
    url = "{}/icsr/search".format(pvbaseuri)
    data = {
    "adverseEvent": "头晕",
    "adverseEventBeginDate": "2019-03-23",
    "adverseEventEndDate": None,
    "adverseEventResult": None,
    "batchNumber": None,
    "brandName": "板蓝根糖",
    "causalityId": None,
    "centerNumber": None,
    "companyId": None,
    "drugType": None,
    "entInfo": None,
    "genericName": None,
    "index": 1,
    "initialOrFollowup": None,
    "isdelete": None,
    "ishideImportReport": None,
    "isinvalid": 0,
    "itemNumber": None,
    "manufacture": None,
    "patientAge": None,
    "patientBirthday": None,
    "patientGender": None,
    "patientName": None,
    "ponderanceId": None,
    "relateNumName": None,
    "relateNumValue": None,
    "reportDrugsafetyDateBegin": None,
    "reportDrugsafetyDateEnd": None,
    "reportReceiveDateBegin": None,
    "reportReceiveDateEnd": None,
    "reportStatus": None,
    "reportType": None,
    "reporterName": None,
    "safetyreportid": None,
    "size": 10,
    "subjectNumber": None,
    "version": None
}

    response = requests.post(url, data=json.dumps(data), headers=login_response)
    util.tool.print_json(response.json())


def icsr(pvbaseuri, login_response, id):
    url = "{}/icsr/{}".format(pvbaseuri, id)
    response = requests.get(url, headers=login_response)
    util.tool.print_json(response.json())


def config_item(pvbaseuri, login_response):
    url = "{}/config/item/getItemsByItemClassIds?String[] itemClassIds=d696ed59-52a1-46bb-ae56-72101abc79bd&String[] itemClassIds=2dfcb1fa-7358-4996-9467-b672fa902d80".format(pvbaseuri)
    response = requests.get(url, headers=login_response)
    util.tool.print_json(response.json())
