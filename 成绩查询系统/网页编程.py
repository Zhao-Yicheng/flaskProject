from flask import Flask,render_template,request
import sqlite3


app=Flask(__name__)

conn = sqlite3.connect('chengjishujuku.db')
cur = conn.cursor()
#cur.execute('create table users("username" TEXT,"psw" TEXT)')
cur.execute('insert into users(username,psw)values("zjz","123")')
conn.commit()

cur.execute('SELECT * FROM users')
li = cur.fetchall()
user={}
list=[]
for line in li:
    for item in line:
        list.append(item)

for i in range(0,len(list),2):
    user[list[i]]=list[i+1]

cur.execute('SELECT * FROM xx成绩表')
temp = cur.fetchall()


@app.route("/")
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    global username
    username=request.form.get("user")
    password=request.form.get("password")
    if username in user and user[username]==password:
        return render_template('index.html',name=username,data=temp)
    else:
        return render_template('login.html')       


@app.route('/select',methods=['POST'])
def select():
    username1=request.form.get("user_sel")
    stuname=[];k=0
    for i in range(len(temp)):
        stuname.append(temp[i][0])
    if username1 in stuname:
        print(username1)
        for j in range(len(stuname)):
            if username1==stuname[j]:
                k=j
                break
        return render_template('select.html', name=username,slt_name=username1,data=temp[k])
cur.close()
if __name__ == "__main__":
    app.run()