# About

This is a small heroku app to bridge between sales delivered in Squarespace and Moodle.
It should allow the course admin to:

- see what sales have happened for what courses listed in Squarespace
- extract info about the purchasers
- push a cohort of users into moodle

# Qucickstart

## Starting the project locally

For Heroku settings info have a look at https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

Running locally using the fish shell

```
> set -x APP_SETTINGS "config.DevelopmentConfig"
> set -x DATABASE_URL "postgresql://localhost/sage"
> set -x BASIC_AUTH_PASSWORD "randompass"
> set -x BASIC_AUTH_USERNAME "randomuser"
> python3 runserver.py 
```




# TODO
TODO: create a test page for the data hub, using example pages from bootstrap  
TODO: create moodle user creation endpoint  
TODO: refactor bridge users so that there is a one to many relationship between emails and course purchases  
TODO: add some testing of endpoints in to the application  
TODO: enable user enrollment to specific courses in moodle  
TODO: show bridge user, and moodle user ID in the bridge app  
TOOD: show which courses someone has purches in SquareSpace  
TODO: add an endpoint for listing courses in moodle  
TODO: add an endpoint for listing SMART product names in the bridge app  
TODO: add some error checking to see if an existing email comes in with a new name  
	think about allowing for name versions / name changes
TODO: setup a model and connection to postgres that maps Squarespace course ids with A2F and moodle course ids  
TODO: get a toy call from the squarespace API working
	blocked by not having access to the API  

# DONE
TODO: sketch a minimal UI to support the application @done  
TODO: figure out how to inspect heroku logs @done  
TODO: create an enpoint that accepts post notifications using HTTP basic Auth
	we can have the resultant data just dump to log if we want at this stage @done  
TODO: prove that we can connect to that endpoint from a google sheets @done  
TODO: push a toy api call into moodle @done(2017-05-18)  

# Moodle Integration

Could get started via the webservices integration

List of plugins

http://ec2-204-236-215-10.compute-1.amazonaws.com/admin/category.php?category=authsettings


Web services authentication - seems the closest but i'm not sure.

https://docs.moodle.org/31/en/Web_services_FAQ
Web services FAQ - MoodleDocs
docs.moodle.org
This document lists some popular questions from the Web Services forum. MNet is used to authenticate some users from a Moodle A site into a Moodle B site. Web ...


# FLASK admin / postgres
https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

# Setup

# Relationship between squarespace transactions, bridge users and moodle users

We are going to make the assumption that the email has to be unique across registrations.
When someone purchases a course on squarepsace we have the following kinds of info about them

PersonIdentier -> email
Person -> email, name
Affiliation -> department, title, other academic related info
Course -> title, instance, transaction

We want to create a moodle user that is a one to one relationship with the Person
who is purchasing the courses.

One person over time can purchase many courses.
They may enter their names differently.

For the simplest demo application we will just create a system that uses only email
to id the user in our bridge system. We can later create a table for person info.



# Testing

Some thoughts on testing:
http://flask.pocoo.org/docs/0.12/testing/
https://www.safaribooksonline.com/library/view/essential-sqlalchemy-2nd/9781491916544/ch04.html
http://alextechrants.blogspot.co.uk/2013/08/unit-testing-sqlalchemy-apps.html
