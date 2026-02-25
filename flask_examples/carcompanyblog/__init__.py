import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

##############################################
### DATABASE SETUP ################3
###########################3
basedir = os.path.abspath(os.pathdirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)

#######LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'user.login'

from carcompanyblog.core.views import core #import blueprint
from carcompanyblog.error_pages.handlers import error_pages #import blueprint

app.register_blueprint(core)
app.register_blueprint(error_pages)