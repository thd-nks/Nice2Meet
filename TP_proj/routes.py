from flask import render_template, request, redirect, url_for
from app import app
from authorization import LogForm
from registration import RegForm
from flask_login import current_user, login_user, logout_user
from models import User


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/reg", methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        name = form.name.data
        surname = form.surname.data
        sex = form.sex.data
        return redirect('/index')
    return render_template('reg.html', form=form)


@app.route("/log", methods=['GET', 'POST'])
def log():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = LogForm()
    if form.validate_on_submit():
        user = User.get(User.login == form.login.data)
        if user is None or not user.check_password(form.password.data):
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
