from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host='db-1.chhkffyll2tw.ap-northeast-2.rds.amazonaws.com', port=3306, user='admin', passwd='12341234', db='flask', charset='utf8')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('back.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'passwd' in request.form:
        result = request.form
        
        username = request.form['username']
        passwd = request.form['passwd']

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND passwd = %s', (username, passwd))
        #account = cursor.fetchone()
        conn.close()

        return render_template('login.html', username=username)

    else:
        return redner_template('back.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)
