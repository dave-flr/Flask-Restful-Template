import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.config.app import DevelopmentConfig, ProductionConfig
from app.resources import HelloWorld

load_dotenv()

# Initializing app
app = Flask(__name__)

# Initializing api
api = Api(app)

# Loading config
config = ProductionConfig() if os.getenv('FLASK_ENV') == 'development' else DevelopmentConfig()
app.config.from_object(config)

# Modules
CORS(app)

# Endpoints
api.add_resource(HelloWorld, '/')
