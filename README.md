Flask-Restful-Template
==================


`Flask-Restful-Template` a workaround to start writing JSON API with all dependencies configured
(PostgreSQL database connection, Basic JWT Authorization) as fast as possible, relies on:

* Flask
* Flask-RESTful
* Psycopg2
* PyJWT

Installation
------------

Create a new virtual environment using `venv`

`python3 -m venv venv`

Activate the environment

`source venv/bin/activate`

Install all dependencies with pip:

`pip install -r requirements.txt`

Run the application

`flask run`

Usage
-----
Starts writing endpoints under `resources/` dir

