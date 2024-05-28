from sqlalchemy import Column, Integer, String
from app.extensions.db import Base
from werkzeug.security import generate_password_hash, check_password_hash
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True,primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(120), unique=False)
    role=Column(String(20), unique=False)

    def __init__(self, username=None, password=None,role=None):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role
        
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username!r}>'