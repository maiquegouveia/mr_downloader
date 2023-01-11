from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = '082b152024defc499646b756c59c9e4d'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\User\Desktop\mrdownloader_website\mrdownloader\mr_downloader.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You need to sign in to access this page'
login_manager.login_message_category = 'alert-info'

from mrdownloader import routes