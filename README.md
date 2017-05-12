# About

This is a small heroku app to bridge between sales delivered in Squarespace and Moodle.
It should allow the course admin to:

- see what sales have happened for what courses listed in Squarespace
- extract info about the purcasers
- push a cohort of users into moodle

# TODO

TODO: setup a model and connection to postgres that maps Squarespace course ids with A2F and moodle course ids
TODO: get a toy call from the squarespace API working
	blocked by not having access to the API
TODO: push a toy api call into moodle
TODO: sketch a minimal UI to support the application

# DONE

TODO: figure out how to inspect heroku logs @done
TODO: create an enpoint that accepts post notifications using HTTP basic Auth
	we can have the resultant data just dump to log if we want at this stage @done
TODO: prove that we can connect to that endpoint from a google sheets @done


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
