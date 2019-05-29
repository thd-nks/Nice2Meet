from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from app import login
from werkzeug.security import check_password_hash
from db_service import db


class Authorization:
    def __init__(self):
        pass

    def check_password(self, user, password):
            return check_password_hash(user.password, password)


@login.user_loader
def load_user(id):
    return db.get_user(id)
    #return User.get(User.id == int(id))


class LogForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


auth = Authorization()
