import moodle_api
import os

moodle_api.URL = os.environ['MOODLE_URL'] #  "http://ec2-204-236-215-10.compute-1.amazonaws.com"
moodle_api.KEY = os.environ['MOODLE_KEY'] # "037a44b63c32f2861d11463c70e20467"

# courses = moodle_api.CourseList()
# print(courses.courses)

api_call = "core_user_create_users"
users = [{
    'username': 'username5', # username must be unique
    'password': 'P-assword5',
    'firstname': 'firstname5',
    'lastname': 'lastname5',
    'email': 'email5@domain.com',
    'customfields': [{'type':'institution', 'value':'harvard'}]
}]

# new_user = moodle_api.call("core_user_create_users", users=users)
# print(new_user)

criteria =  [{
                'key':'email', 'value':'%%'
            }]
users = moodle_api.call("core_user_get_users", criteria=criteria)
print(users)

# User Creation

"""
list of (
object {
username string   //Username policy is defined in Moodle security config.
password string  Optional //Plain text password consisting of any characters
createpassword int  Optional //True if password should be created and mailed to user.
firstname string   //The first name(s) of the user
lastname string   //The family name of the user
email string   //A valid and unique email address
auth string  Default to "manual" //Auth plugins include manual, ldap, imap, etc
idnumber string  Default to "" //An arbitrary ID code number perhaps from the institution
lang string  Default to "en" //Language code such as "en", must exist on server
calendartype string  Default to "gregorian" //Calendar type such as "gregorian", must exist on server
theme string  Optional //Theme name such as "standard", must exist on server
timezone string  Optional //Timezone code such as Australia/Perth, or 99 for default
mailformat int  Optional //Mail format code is 0 for plain text, 1 for HTML etc
description string  Optional //User profile description, no HTML
city string  Optional //Home city of the user
country string  Optional //Home country code of the user, such as AU or CZ
firstnamephonetic string  Optional //The first name(s) phonetically of the user
lastnamephonetic string  Optional //The family name phonetically of the user
middlename string  Optional //The middle name of the user
alternatename string  Optional //The alternate name of the user
preferences  Optional //User preferences
list of (
object {
type string   //The name of the preference
value string   //The value of the preference
}
)customfields  Optional //User custom fields (also known as user profil fields)
list of (
object {
type string   //The name of the custom field
value string   //The value of the custom field
}
)}
)
"""
