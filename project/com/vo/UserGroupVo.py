from project import db
from project import app

class UserGroupVo(db.Model):
    __tablename__ = 'UserGroup'
    GroupId = db.Column(db.Integer, db.ForeignKey('goupMaster.GroupId', ondelete='CASCADE'),primary_key=True)
    GroupName = db.Column('GroupName',db.String(100))
    UserId = db.Column(db.Integer,primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    Status=db.Column('Status',db.Boolean)
    UserName = db.Column('UserName',db.String(50))  

with app.app_context():
    db.create_all()
