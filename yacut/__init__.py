from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .views import main

app.register_blueprint(main)
from .api_views import api

app.register_blueprint(api, url_prefix="/api")

from . import error_handlers
