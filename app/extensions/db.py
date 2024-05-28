from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base,Session

engine = None
db_session : Session = None
Base = None

def init_db(url):
    global engine,db_session,Base
    engine = create_engine(url)
    db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
    Base = declarative_base()
    Base.query = db_session.query_property()
