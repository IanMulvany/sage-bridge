from flask import Flask, render_template, jsonify, request, json
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext.autodoc import Autodoc
from flask_basicauth import BasicAuth
import os
import logging
from datetime import datetime
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
auto = Autodoc(app)
Bootstrap(app)
admin = Admin(app, name='microblog', template_mode='bootstrap3')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import CourseId, SSUser
admin.add_view(ModelView(CourseId, db.session))
admin.add_view(ModelView(SSUser, db.session))

basic_auth = BasicAuth(app)

@app.route('/')
def index():
@auto.doc()
def get_courses():
@auto.doc()
    logger.info("george, we are home")
    return "hola!"

@app.route('/from_gdocs', methods=['POST'])
@basic_auth.required
def gdocs():
@auto.doc()
def index():
@auto.doc()
@auto.doc()
    name = request.form.get("name")
    email = request.form.get("email")
    interest = request.form.get("interest")
    submitted = request.form.get("submitted") # e.g. 5/11/2017 6:47:19
    user = SSUser(name, interest, email, submitted)
    db.session.add(user)
    db.session.commit()
    return("{'I got your back'}")

def create_moodle_user_if_nonexistent(email):


@app.route('/documentation')
def documentation():
    return auto.html()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
