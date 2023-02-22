from project import db
from project import app

class UserVo(db.Model):
    __tablename__ = 'user'
    UserId = db.Column('UserId', db.Integer, primary_key = True)
    FirstName = db.Column('FirstName',db.String(100))
    Emaild=db.Column('Emaild',db.String(100))
    LastName = db.Column('LastName',db.String(100))
    UserName = db.Column('UserName',db.String(50))  
    Password = db.Column('Password',db.String(200))
    GroupOwner = db.Column('GroupOwner',db.Integer)
    InGroup = db.Column('InGroup',db.String(100))
    # 0=user
    # 1=admin
    Role=db.Column('Role',db.Boolean)
    # 0=not approved
    # 1=approved
    Status=db.Column('Status',db.Boolean)


with app.app_context():
    db.create_all()
