# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3
import pandas as pd  #别名
df=pd.read_excel("高二回校考.xlsx")
print(df.at[0,"姓名"])


conn=sqlite3.connect("chengjishujuku.db")
cur=conn.cursor()
cur.execute('CREATE TABLE "xx成绩表" ("姓名"	TEXT,"班级"	TEXT,"总分"	TEXT,"客观分"	TEXT,"主观分"	TEXT)')
for i in range(len(df)):
    a=df.at[i,"姓名"]
    b=df.at[i,"班级"]
    c=df.at[i,"总分"]
    d=df.at[i,"客观分"]
    e=df.at[i,"主观分"]
    cur.execute('INSERT INTO xx成绩表(姓名,班级,总分,客观分,主观分) VALUES("{}","{}","{}","{}","{}")'.format(a,b,c,d,e))
    conn.commit()
cur.execute('SELECT * FROM xx成绩表 ')
data=cur.fetchall()
print(data)
cur.close()

