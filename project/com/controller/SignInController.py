from project import app
from flask import Flask,url_for, render_template, request, flash
from project.com.dao.UserDAO import UserDAO
from project.com.vo.UserVo import UserVo
import re

@app.route('/SignInPage')
def loadSignIn():
    return render_template('SignInPage.html')

@app.route('/signIn',methods=['POST'])
def signInValidation():
    # print('inside sigin')
    vo=UserVo()
    dao=UserDAO()
    FirstName=request.form['FirstName']
    Emaild=request.form['Emaild']
    LastName =request.form['LastName']
    UserName =request.form['UserName']
    Password =request.form['Password']
    # 0=user
    # 1=admin
    # 0=not approved
    # 1=approved
    vo.FirstName =FirstName
    vo.Emaild =Emaild
    vo.LastName = LastName
    vo.UserName =UserName
    vo.Password = Password
    # print(vo)
    # password 
    print(len(FirstName))
    print(len(Emaild))
    print(len(LastName))
    print(len(Password ))
                
    if len(FirstName)>32 or len(Emaild)>32 or len(LastName)>32 or len(UserName)>32 or len(Password)>32:
        print('inside lenght compas')
        flash('you entered very long details, please enter smaller one')
        return render_template('ReloadSignInPage.html',obj=vo)
    vo.Role=0
    if len(Password)<8:
        flash('password should have atleast 8 charcates')
        return render_template('ReloadSignInPage.html',obj=vo)
    if bool(re.search(r"\s", Password)):
        flash('password should not have tab or space in between')
        return render_template('ReloadSignInPage.html',obj=vo)
    if not bool(re.search(r'\d', Password)):
        flash('password should have atleast one digit')
        return render_template('ReloadSignInPage.html',obj=vo)
    if not bool(re.search(r'[A-Z]', Password)):
        flash('password should have atleast one uper case')
        return render_template('ReloadSignInPage.html',obj=vo)
    if not bool(re.search(r'[a-z]', Password)):
        flash('password should have atleast one lower case')
        return render_template('ReloadSignInPage.html',obj=vo)
    
    vo.Status=0
    ans=dao.getUserByUserName(vo.UserName)
    
    if len(ans)>0:
        flash('Please email or username, its already in use!!!')
        return render_template('ReloadSignInPage.html',obj=vo)
    else:   
        dao.addUser(vo)
    return render_template('LoginPage.html')
    