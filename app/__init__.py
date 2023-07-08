from flask import Flask

# instance of Flask application defined in app package accessible as `from app import app`
app = Flask(__name__)

from app import routes
