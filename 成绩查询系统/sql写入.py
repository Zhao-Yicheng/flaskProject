# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:35:53 2022

@author: zhou
"""

import pandas as pd
import sqlite3

df=pd.read_excel("高二回校考.xlsx")
#print(df)

conn=sqlite3.connect('xuesheng.db')
cur=conn.cursor()
'''
cur.execute('create table user ("username" text,"psw" text)')
cur.execute('insert into user(username,psw) values("zjz","123")')
conn.commit()
cur.execute('select * from user')
us=cur.fetchall()
print(us)
'''
#cur.execute('create table chengjibiao("姓名" text,"班级" text,"总分" text,"客观分" text,"主观分" text)')
for i in range(len(df)):
    a=df.at[i,"姓名"]
    b=df.at[i,"班级"]
    c=df.at[i,"总分"]
    d=df.at[i,"客观分"]
    e=df.at[i,"主观分"]
    cur.execute('insert into chengjibiao(姓名,班级,总分,客观分,主观分) values("{}","{}","{}","{}","{}")'.format(a,b,c,d,e))
conn.commit()
cur.execute('select * from chengjibiao')
cjb=cur.fetchall()
print(cjb)

    