from mrdownloader import database, app, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id_user):
    return User.query.get(int(id_user))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    profile_picture = database.Column(database.String, default='default.jpg')