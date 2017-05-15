from flask import Flask, render_template, jsonify, request, json
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
import os
import logging
from datetime import date
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
Bootstrap(app)
admin = Admin(app, name='microblog', template_mode='bootstrap3')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'asff'
db = SQLAlchemy(app)

from models import CourseId, SSUser
admin.add_view(ModelView(CourseId, db.session))
admin.add_view(ModelView(SSUser, db.session))

basic_auth = BasicAuth(app)

@app.route('/')
def index():
    logger.info("george, we are home")
    return "hola!"

@app.route('/from_gdocs', methods=['POST', 'GET'])
@basic_auth.required
def gdocs():
    response_dict = {}
    logger.info("in gdocs looking at values")
    logger.info(request.values)
    logger.info("looking at the data")
    logger.info(request.data)
    logger.info("looking at json")
    # logger.info(request.get_json(force=True))
    logger.info("asusming a GET request")
    logger.info(request.args.get("name"))
    logger.info("asusming a POST request")
    logger.info(request.form.get("name"))
    logger.info("not making assumpotions about the method")
    logger.info(request.values.get("name"))
    return("{'I got your back'}")

@app.route('/test_ingest', methods=['POST'])
def ingest():
    name = request.form.get("name")

    interest = request.form.get("interest")
    logger.info(request.form.get("interest"))
    email = request.form.get("email")
    logger.info(request.form.get("email"))
    created = date.today() # request.form.get("created")
    logger.info(request.form.get("created"))
    user = SSUser(name, interest, email)
    db.session.add(user)
    db.session.commit()
    return("{'I got your back'}")

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

@app.route('/poll_db', methods=['GET'])
def poll():
    "test pulling data from the db about users"
    users = SSUser.query.all()
    # for user in users:
    #     logger.info(user.name)
    return render_template("purchasers.html", users=users)

@app.route('/boot', methods=['GET'])
def boottest():
    return render_template("example.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
