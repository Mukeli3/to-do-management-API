#!/usr/bin/python3
import os
import pymysql
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

pymysql.install_as_MySQLdb()
load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    migrate = Migrate(app, db)
    db.init_app(app)

    from app.routes import todo
    app.register_blueprint(todo)

    with app.app_context():
        from app.model import ToDo
        db.create_all()

    return app