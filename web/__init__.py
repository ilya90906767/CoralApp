from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "coralls.db"




def create_app():
    app = Flask(__name__, template_folder='/home/ilyabetyaev/CollarWeb/web/templates')
    app.config['SECRET_KEY'] = 'hjshjhdjahdfgdsfdss kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    #from .models import Coralls

    with app.app_context():
        db.create_all()
    return app

def create_database(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print('DataBase was created')



