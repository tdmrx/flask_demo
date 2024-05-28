from flask import render_template,request,session,flash
from app.extensions.db import db_session
from app.users import bp
from app.extensions import roles
from app.models.user import User

@bp.route('/users',methods=["GET","POST"])
@roles.allow(groups=["admin"])
def index():
    if request.method == 'POST':
        if request.form.get("set_role",False) != False:
            form_user = request.form.get("username","")
            form_role = request.form.get("role","")
            user = User.query.filter_by(username=form_user).first()
            if user:
                user.role = form_role
                db_session.commit()
                if session["username"] == form_user:
                    session["role"] = form_role
                    session.modified = True
                flash("Success","success")
            else:
                flash("User not found","error")
    users = User.query.all()
    return render_template('users/list.html', users=users)
