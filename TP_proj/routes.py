from flask import render_template, redirect, url_for, jsonify
from app import app
from authorization import LogForm, Authorization
from registration import RegForm, Registration
from profile_service import LocationForm, ProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from models import User
from db_service import db
from chat import ch
from comment_service import cs
from queue_service import queue_service, QueueService


@app.route("/", methods=['GET', 'POST'])
def index():
    logout_user()
    return render_template('index.html')


@app.route("/chat", methods=['GET', 'POST'])
@login_required
def call():
    tlk = ch.get_talks(current_user.id)
    return render_template('chat.html', talks=tlk, id_user=str(current_user.id))


@app.route("/chat/<int:id>", methods=['GET', 'POST'])
def get_msg(id):
    msg = ch.get_messages(current_user.id, id)
    return jsonify(msg, current_user.id)


@app.route("/chat/<int:id_rec>/<string:msg>", methods=['POST'])
def send_msg(id_rec, msg):
    print(msg)
    ch.send_message(current_user.id, id_rec, msg)
    return "done"


@app.route("/chat/<int:idcomment>/<int:mark>/<string:text>", methods=['POST'])
def send_comment(idcomment, mark, text):
    cs.send_comment(current_user.id, idcomment, current_user.name, mark, text)
    return "done"

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
        user = None
        try:
            user = User.get(User.login == form.login.data)
        except User.DoesNotExist:
            pass
        auth = Authorization()
        if user is None or not auth.check_password(user, form.password.data):
            return redirect(url_for('log'))
        login_user(user)
        return redirect(url_for('main_page'))
    return render_template('log.html', form=form)


@app.route("/mainPage", methods=['GET', 'POST'])
@login_required
def main_page():
    queue_service.form_queue(id_user=current_user.id)
    user = queue_service.get_from_queue()

    form = LocationForm()
    if form.validate_on_submit():
        db.update_location(current_user.id, form.location.data)
        return redirect(url_for('main_page'))
    return render_template('mainPage.html', form=form, user=user)


@app.route("/y/<id>", methods=['GET', 'POST'])
@login_required
def say_yes(id):
    if id is None:
        return redirect(url_for('main_page'))
    else:
        db.add_viewed(current_user.id, id)
        db.add_liked(current_user.id, id)
        query = db.get_likes(current_user.id)
        if query.exists():
            db.add_chat(current_user.id, id)
        return redirect(url_for('main_page'))


@app.route("/n/<id>", methods=['GET', 'POST'])
@login_required
def say_no(id):
    if id is None:
        return redirect(url_for('main_page'))
    else:
        db.add_viewed(current_user.id, id)
        return redirect(url_for('main_page'))


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        db.update_profile(current_user.id, form.name.data, form.age.data, form.info.data)
        return redirect(url_for('main_page'))
    return render_template('profile.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
