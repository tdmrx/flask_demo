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

def get_user_tickets(username):
    ret = []
    if isfile(tickets_file):
        with open(tickets_file, 'r') as j:
            jsn = json.loads(j.read())
            for item in jsn:
                if item["from_user"] == username:
                    ret.append(item)
    return ret

def get_for_role(target_role=""):
    ret = []
    if isfile(tickets_file):
        with open(tickets_file, 'r') as j:
            jsn = json.loads(j.read())
            for item in jsn:
                if target_role =="admin":
                    ret.append(item)
                elif item["target"] == target_role:
                    ret.append(item)
    return ret

def create(from_user,text,target):
    ret = False
    jsn = []
    if isfile(tickets_file):
        with open(tickets_file, 'r') as j:
            try:
                jsn = json.loads(j.read())
            except: pass
    jsn.append({"id":str(uuid.uuid4()),"from_user":from_user,"text":text,"target":target,"status":"new"})
    with open(tickets_file, 'w') as j:
        j.write(json.dumps(jsn,indent=1))
        ret = True
    return ret

def assign(id,target):
    ret = False
    jsn = []
    if isfile(tickets_file):
        with open(tickets_file, 'r') as j:
            try:
                jsn = json.loads(j.read())
            except: pass
    for idx,item in enumerate(jsn):
        if item["id"] == id:
            jsn[idx]["target"] = target
            with open(tickets_file, 'w') as j:
                j.write(json.dumps(jsn,indent=1))
            ret = True
    return ret

def set_status(id,status,user_role):
    ret = False
    jsn = []
    if isfile(tickets_file):
        with open(tickets_file, 'r') as j:
            try:
                jsn = json.loads(j.read())
            except: pass
    for idx,item in enumerate(jsn):
        if item["id"] == id:
            
            if item["target"] != user_role:
                if user_role != "admin":
                    ret = False
                    break
            
            jsn[idx]["status"] = status
            with open(tickets_file, 'w') as j:
                j.write(json.dumps(jsn,indent=1))
            ret = True
    return ret



