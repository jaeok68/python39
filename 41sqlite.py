# 파이썬 데이터베이스 프로그래밍
# 데이터의 영속성을 부여하는 방법 중 하나
# 작은 양의 데이터는 파일입출력을 통해 처리 가능
# 대량의 데이터를 체계적으로 저장해서 원하는 목적에 따라
# 데이터를 처리(검색,수정,삭제)할 수 있도록 해 줌

# 파이썬에서는 일반적인 관계형 데이터베이스를 이용해서
# 데이터를 저장,검색,수정,삭제할 수 있음
# 또한, 독립적인 데이터베이스 서버없이 파일기반
# 데이터베이스를 이용해서 간편하게 데이터를 조작할 수도 있음
# 내장형 파일기반 데이터베이스 : sqlite

# sqlite
# 내장형 파일기반 데이터베이스
# 서버가 필요없고 복잡한 설정도 필요없으면서
# 트랜잭션이 지원되는 데이터베이스
# 하나의 파일에 테이블,뷰,색인,트리거등이 저장
# 용량이 작아 메모리에 올리기도 쉽고 속도도 빠른편
# 안드로이드, ios에는 기본적으로 포함되어 있음
# 단, 복잡하고 용량이 큰 데이터를 저장하기에는 다소 적절치 않음
# sqlite.org

# sqlite 설치법
# sqlite-tools-win32-x86-3370200.zip  (2022.2.14기준)
# 압축해제 후 sqlit3.exe를 c:/Java 에 저장
# 명령프롬프트에서 sqlite3.exe를 실행 함
# => cd \Java

# 데이터베이스 생성
# .open 디비명.db
# .open bigdata.db # bigdata.db

# create table member (
#    userid varchar(18) primary key,
#    passwd varchar(18) not null,
#    name varchar(18) not null,
#    email varchar(18) not null
# );

# 테이블 목록 확인 : .table
# 테이블 구조 확인 : pragma table_info('테이블명');

# 테이블 조회시 컬럼헤더 설정
# .header on
# .mode column
# .mode csv

# csv 파일 가져오기
# sqlite>에서 .import
# .mode csv 실행필수
# .import csv파일명 테이블명
# employyes.csv, summermedals.csv
# .import c:/Java/EMPLOYEES_201808111534.csv emp
# .import summermedals.csv medals
# .import zipcode_2013020u.txt zipcode

# tsv 파일 가져오기 - 탭으로 구분된 파일
# .mode tabs
# .import tsv파일명 테이블명
# zipcode -> zipcode

# 데이터 삽입
# insert into member values ('abc123', '987xyz', 'abc123', 'abc@xyz.com');
#
# db종료 : .quit

# 파이썬으로 데이터 다루기 1 - select

import sqlite3

# db연결
conn = sqlite3.connect('C:/Java/bigdata.db')

# SQL 실행을 위해 커서 생성
cur = conn.cursor()

# 실행할 sql문을 작성하고
# 실행후 결과를 커서에 저장
sql = 'select * from member'
cur.execute(sql)
# 반복문을 이용해서 커서에 저장된
# 결과집합으로 부터 한행씩 읽어와서 처리
while True:
    row = cur.fetchone() # 커서에서 한건 읽어온후
    if not row: break   # 내용이 없으면 반복 중단
    
    # 읽어온 결과에서 각 컬럼값을 변수에 저장하고 출력
    result = f'{row[0]} {row[1]} {row[2]} {row[3]}'
    print(result)

# 반복실행 종료시 커서 사용종료
cur.close()

# db 사용종료
conn.close()

# ex) 직책별 사원수 조회
# select * from emp
# EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE,JOB_ID,SALARY,COMMISSION_PCT,MANAGER_ID,DEPARTMENT_ID

# select job_id, count(first_name) cnt from emp
# group by job_id order by cnt desc
import sqlite3

conn = sqlite3.connect('c:/java/bigdata.db')
cur = conn.cursor()

sql = "select job_id, count(employee_id) cnt from emp group by job_id"
cur.execute(sql)

result = ''
while True:
    row = cur.fetchone()
    if not row: break

    result += f'{row[0]} {row[1]}\n'

print(result)

cur.close()
conn.close()

# ex) 국가별 금메달 수상수 조회(상위 10개국만) : medals
# select Country, count(medal) cnt from  medals
# where medal = 'Gold'
# group by Country
# order by cnt desc limit 10
import sqlite3

conn = sqlite3.connect('c:/java/bigdata.db')
cur = conn.cursor()

medal = 'Gold'
sql = f"select country, count(medal) cnt from medals where medal='{medal}' group by Country order by cnt desc limit 10;"
cur.execute(sql)

result = ''
rows = cur.fetchall() # 실행 결과집합 모두 가져옴
for row in rows:
    result += f'{row[0]} {row[1]}\n'

print(result)

cur.close()
conn.close()


# ex) 국가별 금메달 수상수 조회(상위 10개국만) : medals
import sqlite3

conn = sqlite3.connect('c:/java/bigdata.db')
cur = conn.cursor()

sql = "select country, count(medal) cnt from medals where medal='Gold' group by Country order by cnt desc limit 10;"
cur.execute(sql)

while True:
    row = cur.fetchone()
    if not row: break

    result = f'{row[0]} {row[1]}'
    print(result)

cur.close()
conn.close()