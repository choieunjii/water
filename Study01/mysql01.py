import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')
cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS userTable (id char(4) not null primary key, userName varchar(15), email varchar(20), birthYear int)")
# insert문 ""로 감싸야함(''사용X, 사용할 경우 ()안에는 $'로 표시), SQL에서는 쌍따옴표 사용시 오류
# cur.execute("insert into usertable values('Choi', 'CHOIEUNJI', 'choieunji@gmail.com', 1995)") # birth는 숫자이므로 ''사용 안함
try:
    cur.execute("insert into usertable values('Choi', 'CHOIEUNJI', 'choieunji@gmail.com', 1995)")
except:
    conn.rollback()
else:
    conn. commit()
    
#conn.commit() 

conn.close()