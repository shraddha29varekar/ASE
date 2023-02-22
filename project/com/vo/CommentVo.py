from project import db
from project import app

class CommentVo(db.Model):
    __tablename__ = 'CommentVo'
    commentId=db.Column('commentId',db.Integer, primary_key = True)
    commentDescription = db.Column('commentDescription',db.String(100))
    PostId=db.Column('PostId',db.Integer)
    CommentTime=db.Column('comment time',db.DateTime(timezone=True))
    CommentorId=db.Column('CommentorId',db.Integer)
    UserName = db.Column('UserName',db.String(50))  

with app.app_context():
    db.create_all()


