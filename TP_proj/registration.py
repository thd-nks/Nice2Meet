from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, EqualTo
from werkzeug.security import generate_password_hash
from db_service import db


class Registration:
    def __init__(self):
        pass

    def set_password(self, user, password):
            user.password = generate_password_hash(password)


class RegForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    sex = RadioField('Пол', coerce=int, choices=[(1, 'Мужской'), (0, 'Женский')], default=1)
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        if db.get_user_by_login(login.data) is not None:
            raise ValidationError('Login is busy.')
        else:
            pass


register = Registration()
