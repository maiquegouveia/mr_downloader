from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo
from mrdownloader.models import User

class FormRegistration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(6, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    check_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    btn_submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is being used.')
            
class FormLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(6, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    btn_submit = SubmitField('Sign In')