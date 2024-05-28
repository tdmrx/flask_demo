from flask import render_template, redirect, url_for, request,session,flash
from app.login import bp
from app.models.user import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if "logged" in session:
        return redirect(url_for("index"))
    if request.method == 'POST':
        form = request.form
        form_user = form.get("username",False)
        form_pwd = form.get("password",False)
        if form_user and form_pwd:
            user = User.query.filter(User.username == form_user).first()
            if user and user.check_password(form_pwd):
                session["username"] = user.username
                session["logged"] = True
                session["role"] = user.role
                session.modified = True
                return redirect(url_for('index'))
        flash('Invalid Credentials. Please try again.', 'error')
    return render_template('login.html')


@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for("login.login"))