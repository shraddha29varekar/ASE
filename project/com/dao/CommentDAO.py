from project import db
from project.com.vo.CommentVo import CommentVo
from project.com.vo.PostVo import PostVo

vo=CommentVo()
pstvo=PostVo()
class CommentDAO:
    def addComment(self, CommentVo):
        db.session.add(CommentVo)
        db.session.commit()

    def getCommentByPostId(self, PostId):
        comments=CommentVo.query.filter_by(PostId = PostId).all()
        return comments