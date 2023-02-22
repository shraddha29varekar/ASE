from project import app
from project.com.vo.PostVo import PostVo
from project.com.dao.PostDAO import PostDAO
from project.com.dao.UserGroupDAO import UserGroupDAO
from project.com.dao.UserDAO import UserDAO
from project.com.dao.GroupDAO import GroupDAO
from project.com.controller.LoginController import afterApproval,loadDashBoard
from flask import render_template, request
from datetime import datetime as dt

PostDao=PostDAO()
UserGroupDao=UserGroupDAO()
UserDao=UserDAO()
GroupDao=GroupDAO()

@app.route('/LoadAddPost', methods=['POST'])
def LoadAddPost():
    UserId=request.form['UserId']
    approvedGroups=UserGroupDao.getApprovedGroupsByUserId(UserId)
    print(UserId)
    print(approvedGroups)
    if len(approvedGroups)==0:
        approvedGroups=[]
    return render_template('LoadAddPost.html',ln=len(approvedGroups),approvedGroups=approvedGroups,UserId=UserId)

@app.route('/CreatePost', methods=['POST'])
def CreatePost():
    UserId=request.form['UserId']
    GroupId=request.form['GroupId']
    return render_template('AddPost.html',UserId=UserId,GroupId=GroupId)

@app.route('/DeletePost', methods=['POST'])
def deletePost():
    PostId=request.form['PostId']
    PostDao.deletePost(PostId)
    return loadDashBoard()


@app.route('/AddPost', methods=['POST'])
def addPost():
    UserId=request.form['UserId']
    GroupId=request.form['GroupId']
    group=GroupDao.getGroupsByGroupId(GroupId)[0]
    user=UserDao.getByUserId(UserId)
    user=user[0]

    PostDescription=request.form['PostDescription']
    uploaded_img = request.files['file']
    nm=uploaded_img.filename.split('.')
    time=dt.now()
    AdminId=group.AdminId
    vo=PostVo()
    vo.createdTime=time
    vo.CreatorId=UserId
    vo.GroupId=GroupId
    vo.GroupName=group.GroupName
    vo.type=nm[-1]
    vo.Status=0
    vo.PostDescription=PostDescription
    vo.AdminId=AdminId
    vo.UserName=user.UserName
    post=PostDao.addPost(vo,time)
    img=open('../assi3/project/static/'+str(post.PostId)+'.'+nm[-1],'wb')
    img.write(uploaded_img.read())
    img.close()

    return loadDashBoard()

@app.route('/ApprovePost', methods=['POST'])
def approvePost():
    PostId=request.form['PostId']
    # currentUserId=request.form['currentUserId']
    # user=UserDao.getByUserId(currentUserId)
    # user=user[0]
    PostDao.apporvePost(PostId)
    return loadDashBoard() 
