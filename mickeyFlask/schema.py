from flask import Flask

import kangce.user
import kangce.schema

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

isdebug = False

baseUri = "https://www.7csc.com"
pvBaseUri = "{}/pv".format(baseUri)
companyId = "95f05fe5621f4f299771759758ab7fb0"

@app.route('/icsr/schema')
def get_schema(baseUri):
    login_response = kangce.user.login(baseUri, isdebug)
    # kangce.schema.clean_redis(pvBaseUri, login_response, companyId)
    kangce.schema.get_schema(pvBaseUri, login_response)
    kangce.schema.get_schema4add(pvBaseUri, login_response)


if __name__ == "__main__":
    if isdebug:
        baseUri = "http://127.0.0.1:8081"
        pvBaseUri = "{}/".format(baseUri)
    get_schema(baseUri)