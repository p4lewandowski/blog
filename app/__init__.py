from flask import Flask
from config import Config

# instance of Flask application defined in app package accessible as `from app import app`
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
