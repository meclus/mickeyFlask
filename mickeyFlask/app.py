"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask

import kangce.report_setting

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    """Renders a sample page."""
    if name:
        return "Hello %s" % (name)
    else:
        return "Hello World!"

@app.route("/reportsetting/sync")
def sync_report_setting():
    return kangce.report_setting.update()

@app.route("/reportsetting/itemfield/sync")
def sync_report_item_field():
    return kangce.report_setting.update_item_field()

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug = True
    app.run(HOST, PORT)
