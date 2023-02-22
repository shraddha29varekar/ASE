from project import app
from project import db
from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO

from flask import Flask,url_for, render_template, request

dao=UserDAO()
vo=UserVo()

@app.route('/AdminLogin', methods=['POST'])
def adminLogin():
    print('inside adin login............')
    users=dao.getUnApprovedUsers()
    print(len(users))
    return render_template('AdminDashBoard.html',users=users)
@app.route('/admin/approveUser/', methods=['POST'])
def approveUsers():
    print('inside approved user:...')
    name=request.form['UserName']
    user=dao.getUserByUserName(name)
    user[0].Status=1
    dao.addUser(user[0])
    return adminLogin()