from project import db
from project.com.vo.UserVo import UserVo

class UserDAO:
    def addUser(self, UserVo):
        db.session.add(UserVo)
        db.session.commit()

    def deActivateUser(self, UserId):
        user=self.getByUserId(UserId)
        user[0].Status=0
        # db.session.add(user[0])
        db.session.commit()
    
    def getByUserId(self, userId):
        user=UserVo.query.filter_by(UserId = userId).all()
        return user

    def getUserByUserName(self,name):
        user=UserVo.query.filter_by(UserName = name).all()
        return user
        
    def getUserByEmailId(self,email):
        user=UserVo.query.filter_by(EmailId = email).all()
        return user
    def getUnApprovedUsers(self):
        users=UserVo.query.filter_by(Status=0).all()
        return users
    
    def approveUser(self,UserId):
        user=self.getByUserId(UserId)
        user[0].Status=1
        db.session.commit()
        return 1

    def getActiveUsers(self):
        activeUser=UserVo.query.filter_by(Status = 1).filter_by(Role = 0).all()
        print(activeUser)
        return activeUser