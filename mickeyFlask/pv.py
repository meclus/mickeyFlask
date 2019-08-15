from flask import Flask

import time

import kangce.user
import unitTest.icsr

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

isdebug = False

baseUri = "http://dev.7csc.com"
pvBaseUri = "{}/pv".format(baseUri)
companyId = "95f05fe5621f4f299771759758ab7fb0"

@app.route('/icsr/search')
def search_icsr(baseUri):
    login_response = kangce.user.login(baseUri, isdebug)
    unitTest.icsr.search_icsr(pvBaseUri, login_response)

@app.route('/icsr/test')
def test_icsr(baseUri):
    id = "14f9b4094c244b21b4e0de592951d2a2"
    login_response = kangce.user.login(baseUri, isdebug)
    for i in range(20):
        unitTest.icsr.icsr(pvBaseUri, login_response, id)
        time.sleep(1)


@app.route('/config/item/itemclass')
def test_item_class(baseUri):
    login_response = kangce.user.login(baseUri, isdebug)
    unitTest.icsr.config_item(pvBaseUri, login_response)

@app.route('/icsr/r3/validator')
def test_r3_verfity(baseUri):
    id = "97e616aa24d4411a90b5c1d4ab3c1135"
    login_response = kangce.user.login(baseUri, isdebug)
    unitTest.icsr.validator_r3(pvBaseUri, login_response, id)


if __name__ == "__main__":
    if isdebug:
        baseUri = "http://dev.7csc.com/"
        pvBaseUri = "{}/".format(baseUri)
    # test_item_class(baseUri)
    test_r3_verfity(baseUri);