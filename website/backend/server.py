from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import logging

logging.basicConfig(filename="log.log",
                    filemode='a',
                    format='%(asctime)s.%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    level=logging.DEBUG)

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_database(app):
    if not os.path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        logging.info("Database has been created")
        logging.info(f"Database file: {DB_NAME}")


def create_app(base_dir):
    app = Flask(__name__, template_folder=os.path.join(base_dir, "website/frontend/templates"))
    app.config['SECRET_KEY'] = "pOh@*2y=|`sgv]YNu',f9h2_y6MsgD8POE~^(L&.rr'k}!F~Aq*;\"qNc(<ku58^"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from ..frontend.views import views
    from ..frontend.auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")
    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
