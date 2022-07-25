"""Configuration file"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

WAIT_SECONDS = environ.get('WAIT_SECONDS')
INPUT_FILE_LOCATION = path.dirname(path.abspath(__file__)) + '/events.json'
# Running locally - 1:
ENDPOINT = "http://127.0.0.1:4444/event" # python.api grazinti SERVER_NAME

# Running through flask run
# ENDPOINT = "http://127.0.0.1:5000/event" # flask run pakeisti SERVER_NAME

# Running through Docker
# ENDPOINT = "http://api_service:4444/event" # python.api grazinti SERVER_NAME
