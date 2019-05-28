from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Required
from models import User
from werkzeug.security import generate_password_hash


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
        try:
            User.get(User.login == login.data)
            raise ValidationError('Login is busy.')
        except User.DoesNotExist:
            pass


register = Registration()
