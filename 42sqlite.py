# 파이썬으로 데이터 다루기 2 - insert
# 입력한 회원정보를 member 테이블에 저장
import sqlite3

# 회원 정보 입력받기
userid = input('아이디 :')
passwd = input('비밀번호 :')
name = input('이름 : ')
email = input('이메일 : ')

conn = sqlite3.connect('c:/java/bigdata.db')
cur = conn.cursor()

# 아래방식은 비추 - SQL injection 공격의 위험 존재
# sql = 'insert into member values ' \
#      ' (' + userid + ', ' + passwd + ', ' + name +', ' + email + ')'
# sql = f' insert into member values '\
#       f' ({userid}, {passwd}, {name}, {email}); '

# 매개변수 placeholder(?)를 이용해서 실제 값 지정
sql = f' insert into member values (?, ?, ?, ?)'
params = (userid, passwd, name, email)

cur.execute(sql, params) 
conn.commit()   # 테이블에 값 저장하기 위해 commit  호출
print(cur.rowcount, '행이 추가됨')

cur.close()
conn.close()


# 파이썬으로 데이터 다루기 3 - update
# 수정할 회원 아이디 입력받아 회원정보 수정
import sqlite3
conn = sqlite3.connect('c:/java/bigdata.db')
cur = conn.cursor()

# 수정할 아이디 입력후 회원정보 수정
userid = input('수정할 아이디 : ')
passwd = input('새로운 비밀번호 :')
name = input('새로운 이름 : ')
email = input('새로운 이메일 : ')

# named parameter placeholder 이용해서 실제 값 지정
sql = f' update member set passwd = :pwd, '\
      f' name = :name, email = :eml where userid = :uid;'
params = {'pwd':passwd, 'name':name, 'eml':email, 'uid':userid}

cur.execute(sql, params)
conn.commit()
print(cur.rowcount, '행이 수정됨!')

cur.close()
conn.close()


# 파이썬으로 데이터 다루기 4 - delete
# 삭제할 회원 아이디 입력받아 회원정보 삭제
import sqlite3
conn = sqlite3.connect('c:/java/bigdata.db')
cur = conn.cursor()

userid = input('삭제할 아이디 : ')

# named parameter placeholder 이용해서 실제 값 지정
sql = f' delete from member where userid = :uid'
params = {'uid':userid}

cur.execute(sql, params)
conn.commit()
print(cur.rowcount, '행이 삭제됨!')

cur.close()
conn.close()

