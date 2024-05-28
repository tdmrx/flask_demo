from sqlalchemy import Column, Integer, String,Table,ForeignKey
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

def get_user(username):
    ret = False
    if isfile(users_file):
        with open(users_file, 'r') as j:
            jsn = json.loads(j.read())
        for item in jsn:
            if item["username"] == username:
                return item
    return ret

def get_users():
    ret = False
    if isfile(users_file):
        with open(users_file, 'r') as j:
            jsn = json.loads(j.read())
            return jsn
    return ret



def set_role(username,role):
    ret = False
    if isfile(users_file):
        with open(users_file, 'r') as j:
            jsn = json.loads(j.read())
        for idx,item in enumerate(jsn):
            if item["username"] == username:
                jsn[idx]["role"] = role
                with open(users_file, 'w') as j:
                    j.write(json.dumps(jsn))
                break
    return ret