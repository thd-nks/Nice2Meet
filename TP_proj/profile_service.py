from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class ProfileService:
    def __init__(self):
        pass


class LocationForm(FlaskForm):
    location = StringField('Местоположение', validators=[DataRequired()])
    submit = SubmitField('Изменить')


profile = ProfileService()
