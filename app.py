from flask import Flask

from api_blueprint import api, blueprint
from authentication_controller import ns as authentication_namespace

# Primitive placement of web app instance for Gunicorn
# 1) create an instance of the Flask class for this web app
web_app = Flask(__name__)
# 2) initialize the web app
api.add_namespace(authentication_namespace)
api.init_app(blueprint)
web_app.register_blueprint(blueprint)
# 3) configure the web app
# - (e.g. reject incoming requests with a content length greater than following value of bytes) 
web_app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

if __name__ == '__main__':
    # Set the Web App
    web_app.run(host='0.0.0.0', debug=False, threaded=True)
