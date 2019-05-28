from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class Registration:
    def __init__(self):
        pass


class RegForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    sex = RadioField('Пол', choices=[('man', 'Мужской'), ('woman', 'Женский')])
    submit = SubmitField('Зарегистрироваться')


register = Registration()