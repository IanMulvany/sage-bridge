from basic import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from datetime import datetime

class CourseId(db.Model):
    __tablename__ = 'course_map'

    id = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String())
    course_ss_id = db.Column(db.String())
    course_socr_id = db.Column(db.String())
    course_moodle_id = db.Column(db.String())

    def __init__(self, course_title=None, course_ss_id=None, course_socr_id=None, course_moodle_id=None):
        self.course_title = course_title
        self.course_ss_id = course_ss_id
        self.course_socr_id = course_socr_id
        self.course_moodle_id = course_moodle_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

class SSUser(db.Model):
class MoodleUser(db.Model):
    """
    This is a model to capture a Square Space user that gets pushed into
    the system via API.
    """
    __tablename__ = 'moodle_user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    moodle_id = db.Column(db.String())
    moodle_url = db.Column(db.String())
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    bridgeuser_id = db.Column(db.Integer, db.ForeignKey('bridge_user.id'))

    def __init__(self, email=None, moodle_id=None, moodle_url=None):
        self.moodle_id = name
        self.moodle_url = interest
        self.email = email
        self.created = server_default=func.now()

    def __repr__(self):
        return '<id {}>'.format(self.id)

    """
    This is a model to capture a Square Space user that gets pushed into
    the system via API.
    """
    __tablename__ = 'ss_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    interest = db.Column(db.String())
    email = db.Column(db.String())
    submitted = db.Column(db.DateTime())
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, name=None, interest=None, email=None, submitted=None):
        self.name = name
        self.interest = interest
        self.email = email
        self.submitted = submitted
        self.created = server_default=func.now()

    def __repr__(self):
        return '<id {}>'.format(self.id)
