from project import db
from project import app

class GroupVo(db.Model):
    __tablename__ = 'goupMaster'
    GroupId = db.Column('GroupId', db.Integer, primary_key = True)
    GroupName = db.Column('GroupName',db.String(100))
    AdminId = db.Column(db.Integer,nullable=False)
    Status=db.Column('Status',db.Boolean)
    AdminName= db.Column('AdminName',db.String(50))
with app.app_context():
    db.create_all()
