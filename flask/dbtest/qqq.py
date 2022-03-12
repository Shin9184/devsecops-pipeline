import pymysql


conn = pymysql.connect(host='db-1.chhkffyll2tw.ap-northeast-2.rds.amazonaws.com', port=3306, user='admin', passwd='12341234', db='flask', charset='utf8')

username='dsshin'
passwd='1234'

cursor = conn.cursor()
cursor.execute('SELECT * FROM accounts WHERE username = %s AND passwd = %s', (username, passwd))
account = cursor.fetchone()

print(cursor.execute('SELECT * FROM accounts'))

# conn.commit()
conn.close()

