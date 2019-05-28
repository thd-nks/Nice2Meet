from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class Authorization:
    def __init__(self):
        pass


class LogForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


auth = Authorization()