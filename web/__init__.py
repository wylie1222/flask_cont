import os
from flask import Flask
from flask_migrate import Migrate

def create_app(testconfig=None):
    app = Flask(__name__, instance_relative_config=True)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@pg:5432/football_teamdb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/football_teamdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)
    
    
    @app.route('/')
    def home():
        return 'Welcome to the home page'

    return app
