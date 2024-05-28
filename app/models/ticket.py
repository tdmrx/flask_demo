from sqlalchemy import Column, Integer, String
from app.extensions.db import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True,autoincrement=True)
    from_user = Column("from_user",String(50))
    text = Column('text',String(120), unique=False)
    role = Column('role',String(120), unique=False)
    status = Column('status',String(10), unique=False)

    def __init__(self,from_user=None,text=None, role=None,status=None):
        self.from_user = from_user
        self.text = text
        self.role = role
        self.status = status

    def __repr__(self):
        return f'<User {self.name!r}>'
