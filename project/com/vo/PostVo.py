from project import db
from project import app
# from project.com.vo import groupVo

# groupObj =groupVo()
class PostVo(db.Model):
    __tablename__ = 'postMaster'
    PostId=db.Column('PostId', db.Integer, primary_key = True)
    GroupId = db.Column('GroupId', db.Integer,nullable=False)
    GroupName = db.Column('GroupName', db.Integer,nullable=False)
    CreatorId = db.Column(db.Integer,nullable=False)
    type=db.Column('type',db.String(100))
    createdTime=db.Column(db.DateTime(timezone=True))
    Status=db.Column('Status',db.Boolean)
    AdminId = db.Column('AdminId',db.Integer,nullable=False)
    UserName = db.Column('UserName',db.String(50))  
    PostDescription=db.Column('PostDescription',db.String(500))

with app.app_context():
    db.create_all()
