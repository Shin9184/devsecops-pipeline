from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host='db-1.chhkffyll2tw.ap-northeast-2.rds.amazonaws.com', port=3306, user='admin', passwd='12341234', db='flask', charset='utf8')

cursor=conn.cursor()

sql = "INSERT INTO accounts(username,passwd) VALUES('test','test')"
cursor.execute(sql)

print(cursor.execute('SELECT * FROM accounts'))

conn.commit()
conn.close()
