from project import app
from project import db
from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO
from project.com.dao.GroupDAO import GroupDAO
from project.com.dao.PostDAO import PostDAO
from project.com.dao.UserGroupDAO import UserGroupDAO



from flask import Flask,url_for, render_template, request

UserDao=UserDAO()
vo=UserVo()
GroupDao=GroupDAO()
PostDao=PostDAO()
UserGroupDao=UserGroupDAO()
# @app.route('/AdminLogin', methods=['POST'])

def adminLogin():
    print('inside adin login............')
    users=UserDao.getUnApprovedUsers()
    print(len(users))
    return users
@app.route('/admin/approveUser', methods=['POST'])
def approveUsers():
    print('inside approved user:...')
    UserId=request.form['TargetUserId']
    UserDao.approveUser(UserId)
    print('in load dashboard.............')
    UserId=request.form['UserId']
    user=UserDao.getByUserId(UserId)
    print(UserId)
    print(user)
    # print(user[0])
    user=user[0]
    # return afterApproval(user)
    unApprovedUserList=[]
    unApprovedGroupUserList=[]
    UnApprovedPostList=[]
    activeGroupUser=[]
    unApprovedGroup=[]
    dailyPost=[]
    adminPost=[]
    groupPost=[]
    activeUsers=[]
    vo=UserVo()
    dao=UserDAO()
    # user=user[0]
    print(user)
    if user.Status==1:
        adminGroups=GroupDao.getGroupsWhereAdminId(user.UserId)
        group=UserGroupDao.getApprovedGroupsByUserId(user.UserId)
        if user.Role==1:
            activeUsers=UserDao.getActiveUsers()
            print('activeUsers',activeUsers)
            # activeGroup=GroupDao.activeGroups()
            unApprovedUserList=adminLogin()
            unApprovedGroup=GroupDao.UnApporvedGroup()
            UnApprovedPostList=PostDao.getUnapporvedPost()
            activeGroupUser=GroupDao.activeGroups()

            unApprovedGroupUserList=UserGroupDao.getUnapporvedUser()
            adminPost=PostDao.getApporvedPost()
            print('admin post....',adminPost)
        # check if user is admin of any group
        elif len(adminGroups)>0:
            for i in adminGroups:
                ls=PostDao.getUnapporvedPostByGroupId(i.GroupId)
                # ps=PostDao.getApporvedPostByGoupId(i.GroupId)
                # if len(ps)>0:
                #     dailyPost.append(ps)
                if len(ls)>0:
                    UnApprovedPostList.append(ls)
                users=UserGroupDao.getUnapporvedUserByGroupId(i.GroupId)
                if len(users):
                    unApprovedGroupUserList.append(users)
        if len(group)>0:
            for j in group:
                ps=PostDao.getApporvedPostByGoupId(j.GroupId)
                if len(ps)>0:
                    groupPost.append(ps)
                # ps=PostDao.getApporvedPostByGoupId(i.GroupId)
        print('user role:',user.Role)
        # return render_template('DashBoard.html',obj=user,activeGroup=activeGroup,lenActiveGroup=len(activeGroup),lenActiveUsers=len(activeUsers),activeUsers=activeUsers,adminPost=adminPost,ldp=len(groupPost),lugu=len(unApprovedGroupUserList),lug=len(unApprovedGroup),lup=len(UnApprovedPostList),lus=len(unApprovedUserList),dailyPost=groupPost,unApprovedUserList=unApprovedUserList,UnApprovedPostList=UnApprovedPostList,unApprovedGroup=unApprovedGroup,unApprovedGroupUserList=unApprovedGroupUserList)
        return render_template('DashBoard.html',obj=user,activeGroupUser=activeGroupUser,lenActiveGroupUser=len(activeGroupUser),lenActiveUsers=len(activeUsers),activeUsers=activeUsers,adminPost=adminPost,ldp=len(groupPost),lugu=len(unApprovedGroupUserList),lug=len(unApprovedGroup),lup=len(UnApprovedPostList),lus=len(unApprovedUserList),dailyPost=groupPost,unApprovedUserList=unApprovedUserList,UnApprovedPostList=UnApprovedPostList,unApprovedGroup=unApprovedGroup,unApprovedGroupUserList=unApprovedGroupUserList)

    else:
        return render_template('LoginPage.html')