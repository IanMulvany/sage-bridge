from flask import Flask, render_template, jsonify
from flask_basicauth import BasicAuth
import os
import requests as r

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'asff'

basic_auth = BasicAuth(app)

@app.route('/')
def index():
    return "hola!"

@app.route('/secret')
@basic_auth.required
def secret_view():
    return render_template('secret.html')

@app.route('/testr', methods=['GET'])
def requests():
    test_url = "https://api.crossref.org/works/10.1037/0003-066X.59.1.29/agency"
    # return jsonify(test_url)
    response = r.get(test_url)
    return (response.text, response.status_code, response.headers.items())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
