from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "daytrade.db"
#Server as starting all necessary connections for a website after running a website

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #configure the database with app
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .func import func

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(func, url_prefix='/')

    from .models import User, Note

    create_database(app)
    # login_manager is the central of login function, must defines beforehand 
    login_manager = LoginManager()
    #configure the login fucntion on all functions in auth library
    login_manager.login_view = 'auth.login'
    #configure the login manager with app
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')