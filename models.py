from basic import db
from sqlalchemy.dialects.postgresql import JSON
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
    """
    This is a model to capture a Square Space user that gets pushed into
    the system via API.
    """
    __tablename__ = 'ss_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    interest = db.Column(db.String())
    email = db.Column(db.String())
    submitted = db.Column(db.Date())
    created = db.Column(db.Date())
    # created_at = db.Column(db.DateTime)

    def __init__(self, name=None, interest=None, email=None, submitted=None, created=None):
        self.name = name
        self.interest = interest
        self.email = email
        self.submitted = submitted
        self.created = created

    def __repr__(self):
        return '<id {}>'.format(self.id)
