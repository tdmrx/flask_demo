from flask import Flask,render_template,session
#необхідно для server side sessions
from flask_session import Session
from os.path import join,isfile
from config import Config,basedir
from app.extensions import roles
from app.extensions import db
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    app.config['SESSION_PERMANENT'] = True
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config["SESSION_REFRESH_EACH_REQUEST"] = False
    app.config['SESSION_FILE_THRESHOLD'] = 100  

    app.config['SECRET_KEY'] = Config.SECRET_KEY
    sess = Session()
    sess.init_app(app)
    
    db.init_db(Config.SQLALCHEMY_DATABASE_URI)
    
    if not isfile(join(basedir,"app.db")):
        from app.extensions.db import db_session,engine,Base
        from app.models.user import User
        from app.models.ticket import Ticket
        #val = Base.metadata.tables.values()
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        db_session.add(User("admin","admin","admin"))
        db_session.add(User("manager","manager","manager"))
        db_session.add(User("analyst","analyst","analyst"))
        db_session.add(User("user","user","user"))
        db_session.commit()

    from app.tickets import bp as tickets_bp
    app.register_blueprint(tickets_bp)
    from app.login import bp as login_bp
    app.register_blueprint(login_bp)
    from app.users import bp as users_bp
    app.register_blueprint(users_bp)
    
    @app.route('/')
    @roles.logged
    def index():
        return render_template("home.html")
        
    @app.before_request
    def make_session_permanent():
        session.permanent = True
        

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.db_session.remove()
    return app