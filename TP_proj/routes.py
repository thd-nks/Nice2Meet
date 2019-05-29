from flask import render_template, request, redirect, url_for
from app import app
from authorization import LogForm, Authorization
from registration import RegForm, Registration
from flask_login import current_user, login_user, logout_user
from models import User


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/test")
def call():
    return render_template('chat.html')

@app.route("/reg", methods=['GET', 'POST'])
def reg():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = RegForm()
    if form.validate_on_submit():
        reg = Registration()
        user = User(name=form.name.data, sex=form.sex.data, age=form.age.data, rating=0,
                    location='', info='', picture='', login=form.login.data)
        reg.set_password(user, form.password.data)
        user.save()
        return redirect(url_for('log'))
    return render_template('reg.html', form=form)


@app.route("/log", methods=['GET', 'POST'])
def log():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = LogForm()
    if form.validate_on_submit():
        user = User.get(User.login == form.login.data)
        auth = Authorization()
        if user is None or not auth.check_password(user, form.password.data):
            return redirect(url_for('log'))
        login_user(user)
        return redirect(url_for('main_page'))
    return render_template('log.html', form=form)


@app.route("/mainPage", methods=['GET', 'POST'])
def main_page():
    return render_template('mainPage.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
