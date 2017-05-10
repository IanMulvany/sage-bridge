from flask import Flask, render_template, jsonify, request
from flask_basicauth import BasicAuth
import os
import logging
#  from logging.config import fileConfig
import requests as r

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'asff'

basic_auth = BasicAuth(app)

@app.route('/')
def index():
    logger.info("george, we are home")
    return "hola!"

@app.route('/from_gdocs', methods=['POST','GET'])
@basic_auth.required
def gdocs():
    logger.info("in gdocs")
    logger.info(request.json)
    return jsonify(request.json)

@app.route('/secret')
@basic_auth.required
def secret_view():
    return render_template('secret.html')

@app.route('/testr', methods=['GET'])
@basic_auth.required
def requests():
    test_url = "https://api.crossref.org/works/10.1037/0003-066X.59.1.29/agency"
    # return jsonify(test_url)
    response = r.get(test_url)
    return (response.text, response.status_code, response.headers.items())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
