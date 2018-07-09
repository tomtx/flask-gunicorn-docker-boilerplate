from flask import Blueprint
from flask_restplus import Api

API_DESCRIPTION = "This is a boilerplate for containerized Python backend app with Flask as a Python micro web framework, " \
                  "Gunicorn as a Python Web Server Gateway Interface (WSGI) HTTP server, and with Docker as a container " \
                  "technology to package up this application."

blueprint = Blueprint('Python App Boilerplate', __name__, url_prefix='/app')

api = Api(version='0.1', title="""Python App Boilerplate""", description=API_DESCRIPTION)
