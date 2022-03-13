from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host='db-1.chhkffyll2tw.ap-northeast-2.rds.amazonaws.com', port=3306, user='admin', passwd='12341234', db='flask', charset='utf8')

def db_conn():
    conn = pymysql.connect(host='db-1.chhkffyll2tw.ap-northeast-2.rds.amazonaws.com', port=3306, user='admin', passwd='12341234', db='flask', charset='utf8')
    cursor = conn.cursor()
    sql = '''SELECT * FROM accounts;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return str(result)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = str(request.form['username'])
        passwd = str(request.form['passwd'])
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE username=%s AND passwd=%s",(username,passwd))
        account = cursor.fetchone()
        
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']

        return render_template('user_home.html',username=session['username'])

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')
        
@app.route('/user_register', methods=['GET','POST'])
def user_register():
    if request.method == 'POST':
        username = str(request.form['username'])
        passwd = str(request.form['passwd'])

        cursor = conn.cursor()
        cursor.execute("INSERT INTO accounts (username,passwd) VALUES(%s,%s)",(username,passwd))
        conn.commit()
        conn.close()

        return render_template('index.html')

@app.route('/user_home', methods=['GET','POST'])
def user_home():
    return render_template('user_home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug = True)
