from project import db
from project.com.vo.UserGroupVo import UserGroupVo
from project.com.vo.groupVo import GroupVo

class UserGroupDAO:
    def addUserGroup(self, vo):
        print('add iuser group.......')
        print(vo.GroupId,vo.UserId)
        db.session.add(vo)
        db.session.commit()

    def addUserGroupAdmin(self, vo):
        print('add iuser group.......')
        print(vo.GroupId,vo.UserId)
        vo.Status=1
        db.session.add(vo)
        db.session.commit()
    
    def getByUserId(self,userId):
        groups=UserGroupVo.query.filter_by(UserId = userId).all()
        return groups
    
    def getByUserIdGroupId(self,userId,GroupId):
        groups=UserGroupVo.query.filter_by(UserId = userId).filter_by(GroupId = GroupId).all()
        return groups
   
    def getApprovedGroupsByUserId(self,userId):
        req=[]
        approvedGroups=UserGroupVo.query.filter_by(UserId = userId).filter_by(Status=1).all()
        for gr in approvedGroups:
            g=GroupVo.query.filter_by(GroupId = gr.GroupId).all()
            if g[0].Status==1:
                req.append(gr)
        return req
    
    def getUnapporvedUserByGroupId(self, GroupId):
        unApprovedUsers=UserGroupVo.query.filter_by(GroupId = GroupId).filter_by(Status = 0).all()
        return unApprovedUsers
    
    def getUnapporvedUser(self):
        unApprovedUsers=UserGroupVo.query.filter_by(Status = 0).all()
        return unApprovedUsers
    
    def apporveUser(self,vo):
        groups=self.getByUserIdGroupId(vo.UserId,vo.GroupId)
        groups[0].Status=1
        db.session.commit()
        return 1
    
