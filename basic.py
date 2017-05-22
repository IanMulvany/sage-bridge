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
admin = Admin(app, name='SageBridge', template_mode='bootstrap3')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import CourseId, SSTransaction, BridgeUser, MoodleUser
admin.add_view(ModelView(CourseId, db.session))
admin.add_view(ModelView(SSTransaction, db.session))
admin.add_view(ModelView(BridgeUser, db.session))
admin.add_view(ModelView(MoodleUser, db.session))
basic_auth = BasicAuth(app)

@app.route('/')
def index():
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

class ProcessingError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(ProcessingError)
def handle_processing_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


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
# @app.route('/from_gdocs', methods=['POST'])
# @basic_auth.required
# def gdocs():
#     name = request.form.get("name")
#     email = request.form.get("email")
#     interest = request.form.get("interest")
#     submitted = request.form.get("submitted") # e.g. 5/11/2017 6:47:19
#     user = SSUser(name, interest, email, submitted)
#     db.session.add(user)
#     db.session.commit()
#     return("{'I got your back'}")
@app.route('/create_ss_transaction', methods=['POST'])
# @basic_auth.required
@auto.doc()
def create_ss_transaction():
    """
    create a record of a squarespace transation in the brige app.
    """
    # try:
    name = request.form.get("name")
    email = request.form.get("email")
    interest = request.form.get("interest")
    submitted = request.form.get("submitted") # e.g. 5/11/2017 6:47:19
    ss_transaction = SSTransaction(name, interest, email, submitted)
    # check if bridge user exists with this email
    bridge_user = create_or_get_bridge_user(email)
    associate_bridge_user_transaction(bridge_user, ss_transaction)
    db.session.add(ss_transaction)
    db.session.commit()
    return jsonify("transaction created in the bridge app", 200)
    # except:
    #     message = "something failed in the function"
    #     logger.info(message)
    #     raise ProcessingError(message)

def create_moodle_user_if_nonexistent(email):
    """
    given an email
    check if we have a moodle user record for this email locally
    check if moodle already has a user with the email
        if so check for potential problems, re name drift
    if neither above occurs, then create this new user in moodle
    """
    bridge_user = create_or_get_bridge_user(email)
    moodle_user = create_or_get_moodle_user(email)
    associate_bridge_user_moodle_user(bridge_user, moodle_user)
    # check if there is already a moodle user with this email.
    criteria =  [{
                    'key':'email', 'value':email
                }]
    users = moodle_api.call("core_user_get_users", criteria=criteria)
    if uses == None:
        api_call = "core_user_create_users"
        users = [{
            'username': 'username5', # username must be unique
            'password': 'P-assword5',
            'firstname': 'firstname5',
            'lastname': 'lastname5',
            'email': email,
            'customfields': [{'type':'institution', 'value':'harvard'}]
        }]

        new_user = moodle_api.call("core_user_create_users", users=users)

    criteria =  [{
                    'key':'email', 'value':email
                }]
    users = moodle_api.call("core_user_get_users", criteria=criteria)

    url = users[0].url
    moodle_id = users[0].moodle_id

    # TODO: unfuck this function
    moodle_user = MoodleUser(email, moodle_id, moodle_url)

    return True



@app.route('/create_moodle_users', methods=['POST'])
# @basic_auth.required
@auto.doc()
def create_moodle_users():
    """
    create a record of a squarespace transation in the brige app.
    """
    emails = request.form.getlist("cb[]")
    for email in emails:
        create_moodle_user_if_nonexistent(email.rstrip("\")): #noticed that there is a trailing backslask on form data?
    return jsonify("got emails", 200)

@app.route('/create_moodle_users_view', methods=['GET'])
# @basic_auth.required
def create_moodle_users_view():
    """
    show all bridge uses
    allow the admin to select bridge users
    create moodle users based on the selected brdige users
    """
    bridge_users = BridgeUser.query.all()
    return render_template("create_moodle_users.html", users=bridge_users)

@app.route('/documentation')
def documentation():
    return auto.html()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
