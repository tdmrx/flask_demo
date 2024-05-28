from flask import g, request, redirect, url_for,session,render_template,flash
from app.extensions.db import db_session
from app.tickets import bp
from app.extensions import roles
from app.models.ticket import Ticket

@bp.route('/tickets')
@roles.deny(groups=["user"])
def index():
    if session["role"] == "admin":
        tickets = Ticket.query.all()
    else:
        tickets = Ticket.query.filter(Ticket.role == session["role"])
    return render_template('tickets/list.html', tickets=tickets,role=session["role"])

@bp.route('/tickets/my')
@roles.allow(groups=["user"])
def user_tickets():
    tickets = Ticket.query.filter(Ticket.from_user == session["username"])
    return render_template('tickets/user_list.html', tickets=tickets,role=session["role"])

@bp.route('/tickets/assign',methods=["POST"])
@roles.allow(groups=["admin"])
def assign_ticket():

    ticket_id = request.form.get("id","")
    target = request.form.get("target","")
    ticket = Ticket.query.filter(Ticket.id == ticket_id).first()
    if ticket:
        ticket.role = target
        try:
            db_session.commit()
            flash("Success","success")
        except:
            flash("Error","error")
    else:
        flash("Success","success")
    return redirect(url_for("tickets.index"))


@bp.route('/tickets/status',methods=["POST"])
@roles.deny(groups=["user"])
def set_status():
    
    ticket_id = request.form.get("id","")
    status = request.form.get("status","")
    if session["role"] == "admin":
        ticket = Ticket.query.filter(Ticket.id == ticket_id).first()
    else:
        ticket = Ticket.query.filter(Ticket.id == ticket_id,Ticket.role == session["role"]).first()
    if ticket:
        ticket.status = status
        try:
            db_session.commit()
            flash("Success","success")
        except:
            flash("Error","error")
    else:
        flash("Success","success")
        
    return redirect(url_for("tickets.index"))

@bp.route('/tickets/create',methods=["GET","POST"])
@roles.allow(groups=["user"])
def create_ticket():
    error = None
    if request.form.get("submit_ticket",False) != False:
        form_target = request.form.get("target","")
        form_text = request.form.get("text","")
        ticket = Ticket(session["username"],form_text,form_target,"pending")
        try:
            db_session.add(ticket)
            db_session.commit()
            flash("Success","success")
        except:
            flash("Error","error")
    return render_template('tickets/create.html', error=error)
