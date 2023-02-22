from project import app
from project import db
from project.com.vo.groupVo import GroupVo
from project.com.vo.UserGroupVo import UserGroupVo
from project.com.dao.GroupDAO import GroupDAO
from project.com.dao.UserGroupDAO import UserGroupDAO
from project.com.dao.UserDAO import UserDAO
from project.com.controller.LoginController import afterApproval,loadDashBoard
from flask import Flask,url_for, render_template, request,redirect



groupDao=GroupDAO()
UserGroupDao=UserGroupDAO()
userDao=UserDAO()

@app.route('/LoadCreateGroup', methods=['POST'])
def LoadCreatingGroup():
    print('inside load create groups.......')
    UserId=request.form['UserId']
    UserId=UserId
    print(UserId)
    return render_template('LoadCreateGroup.html',UserId=UserId)

@app.route('/createGroup', methods=['POST'])
def addGroup():
    UserId=request.form['UserId']
    vo=GroupVo()
    vo.GroupName=request.form['GroupName']
    user=userDao.getByUserId(UserId)
    user=user[0]
    vo.AdminId=UserId
    vo.Status=0
    vo.AdminName=user.UserName
    groupDao.addGroup(vo)
    grp=groupDao.getGroupsByGroupname(vo.GroupName)[0]

    vo=UserGroupVo()
    vo.UserId=UserId
    vo.GroupId=grp.GroupId
    vo.GroupName=grp.GroupName
    vo.Status=1
    vo.AdminId=UserId
    vo.UserName=user.UserName

    UserGroupDao.addUserGroup(vo)
    # print(user[0].UserName)
    return loadDashBoard()

# join group
@app.route('/LoadJoinGroup', methods=['POST'])
def loadJoinGroup():
    UserId=request.form['UserId']
    groups=groupDao.getAllGroup()
    AlreadyInGroup=UserGroupDao.getByUserId(UserId)
    req=[]
    for j in range(len(groups)):
        flg=False
        for k in AlreadyInGroup:
            if groups[j].GroupId==k.GroupId:
                flg=True
        if not flg:
            req.append(groups[j])


    return render_template('LoadJoinGroups.html',groups=req,UserId=UserId)

@app.route('/JoinGroup', methods=['POST'])
def joinGroup():
    UserId=request.form['UserId']
    user=userDao.getByUserId(UserId)
    user=user[0]
    GroupId=request.form['GroupId']
    GroupName=request.form['GroupName']
    grpInfo=groupDao.getGroupsByGroupId(GroupId)[0]
    vo=UserGroupVo()
    vo.GroupId=GroupId
    vo.UserId=UserId
    vo.GroupName=GroupName
    vo.Status=0
    vo.UserName=user.UserName
    vo.AdminId=grpInfo.AdminId
    UserGroupDao.addUserGroup(vo)
    return loadJoinGroup()

@app.route('/ApproveUserForGroup', methods=['POST'])
def addUserToGroup():
    print('inside ApproveUserForGroup')
    UserId=request.form['TargetUserId']
    print(UserId)
    user=userDao.getByUserId(UserId)
    user=user[0]
    GroupId=request.form['GroupId']
    # currentUserId=request.form['UserId']
    vo=UserGroupVo()
    vo.UserId=UserId
    vo.GroupId=GroupId
    vo.UserName=user.UserName
    UserGroupDao.apporveUser(vo)
    print('after get UserBy Id')
    print('user',user)
    return loadDashBoard()

@app.route('/ApproveGroup', methods=['POST'])
def approveGroup():
    print('inside ApproveUserForGroup')
    GroupId=request.form['GroupId']
    # currentUserId=request.form['currentUserId']
    vo=GroupVo()
    vo.GroupId=GroupId
    groupDao.apporvedGroup(GroupId)
    # user=userDao.getByUserId(currentUserId)
    # print('user',user)
    return loadDashBoard()


@app.route('/DeActivateGroup', methods=['POST'])
def DeActivateGroup():
    GroupId=request.form['GroupId']
    groupDao.DeActivateGroup(GroupId)
    return loadDashBoard()


