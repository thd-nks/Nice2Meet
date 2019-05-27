from flask import render_template, request, redirect, url_for
from app import app
from authorization import LogForm
from registration import RegForm


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
    form = LogForm()
    return render_template('log.html', form=form)
