# About

This is a small heroku app to bridge between sales delivered in Squarespace and Moodle. 
It should allow the course admin to:

- see what sales have happened for what courses listed in Squarespace 
- extract info about the purcasers 
- push a cohort of users into moodle 

# TODO

TODO: get a toy call from the squarespace API working 
TODO: setup a model and connection to postgres that maps Squarespace course ids with A2F and moodle course ids 
TODO: push a toy api call into moodle 
TODO: figure out how to inspect heroku logs 
TODO: create an enpoint that accepts post notifications using HTTP basic Auth 
	we can have the resultant data just dump to log if we want at this stage 
TODO: prove that we can connect to that endpoint from a google sheets 
TODO: skets a minmal UI to support the application 
