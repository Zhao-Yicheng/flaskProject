from flask import Flask,render_template,request,redirect,url_for
import flask
from sql import *
app = Flask(__name__)


@app.route("/")
def hello_world():
    return redirect('login')

@app.route('/login',methods=['GET','POST'])
def user_login():
    if request.method=='POST':  # 注册发送的请求为POST请求
        username = request.form['username']
        password = request.form['password']
        if username=='' and password=='':
            login_massage = "温馨提示：账号和密码是必填"
            return render_template('login.html', message=login_massage)
        elif is_existed(username, password):
            return render_template('index.html', username=username)
        elif exist_user(username):
            login_massage = "温馨提示：密码错误，请输入正确密码"
            return render_template('login.html', message=login_massage)
        else:
            login_massage = "温馨提示：不存在该用户，请先注册"
            return render_template('login.html', message=login_massage)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
