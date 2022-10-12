# ex) 주민번호에서 생년과 월,일, 성별을 추출해서
# 각 변수에 적절히 저장하세요
jumin = '2205094123456'

# if int(jumin[0:2]) < 21 and int(jumin[6]) in (3,4):
if int(jumin[6]) in (3,4):
    year = 2000 + int(jumin[:2])
else:
    year = 1900 + int(jumin[0:2])
month = int(jumin[2:4])
day = int(jumin[4:6])
gender = int(jumin[6:7])
# 성별 탐색
if gender in (1,3):
    gender = '남자'
else:
    gender = '여자'

print(f'{year:d}년 {month:d}월 {day:d}일 {gender:s}')

# 12 - 시간계산
time = 1234567890
days = time // 86400

time = 98765
hours = time // 3600

time = 1234
mins = time // 60

print(f'days : {days:d} hours : {hours:d} mins : {mins:d}' )

# 16 - 잔돈계산
# 비용과 지불금액을 입력받아 잔돈 계산

# 지불 금액은 ??? 원 이고,
# 받은 금액은 ??? 원 이고
# 잔액은 ???원 입니다
cost = 12340
money = 50000
charge = money - cost # 37660
# 50,000원권 계산
w50k = int(charge / 50000)
charge = charge - (w50k * 50000)
print(f'w50k : {w50k:d}')

# 10,000원권 계산
w10k = int(charge / 10000)
charge = charge - (w10k * 10000)
print(f'w10k : {w10k:d}')

# 5,000 원권 계산
w5k = int(charge / 5000)
charge = charge - (w5k * 5000)
print(f'w5k : {w5k:d}')

# 1,000 원권 계산
w1k = int(charge / 1000)
charge = charge - (w1k * 1000)
print(f'w1k : {w1k:d}')

# 500 원 계산
w5m = int(charge / 500)
charge = charge - (w5m * 500)
print(f'w5m : {w5m:d}')

# 100원 계산
w1m = int(charge / 100)
charge = charge - (w1m * 100)
print(f'w1m : {w1m:d}')

# 50원 계산
w50 = int(charge / 50)
charge = charge - (w50 * 50)
print(f'w50 : {w50:d}')

# 10원 계산
w10 = int(charge / 10)
charge = charge - (w10 * 10)
print(f'w10 : {w10:d}')

# 결과 출력
print(w50k, w10k, w5k, w1k, w5m, w1m, w50, w10)

# 파이썬에서 제공하는 몫/나머지 연산자를 이용하면
# 수식이 좀 더 간단해짐
cost = int(input('비용 : '))
money = int(input('지불금액 : '))
charge = money - cost  # 37660

# 결과 출력
print(f'''
지불금액은 {cost}원 이고,
받은 금액은 {money}원 이고
잔액은 {charge}원 입니다.
''')

# 50,000원권 계산
w50k = charge // 50000
charge = charge % 50000
print(f'w50k : {w50k:d}')

# 10,000원권 계산
w10k = charge // 10000
charge = charge % 10000
print(f'w10k : {w10k:d}')

# 5,000 원권 계산
w5k = charge // 5000
charge = charge % 5000
print(f'w5k : {w5k:d}')

# 1,000 원권 계산
w1k = charge // 1000
charge = charge % 1000
print(f'w1k : {w1k:d}')

# 500 원 계산
w5m = charge // 500
charge = charge % 500
print(f'w5m : {w5m:d}')

# 100원 계산
w1m = charge // 100
charge = charge % 100
print(f'w1m : {w1m:d}')

# 50원 계산
w50 = charge // 50
charge = charge % 50
print(f'w50 : {w50:d}')

# 10원 계산
w10 = charge // 10
charge = w10 % 10
print(f'w10 : {w10:d}')



print(f'''
50,000 원권은 {w50k}장, 10,000원권은 {w10k}장,
5,000원권은 {w5k}장, 1,000원권은 {w1k}장
500원은 {w5m}개, 100원은 {w1m}개
50원은 {w50}개, 10원은 {w10}개 입니다.
''')



#cost = int(input('지불 금액 : '))
#money = int(input('받은 금액 : '))
#charge = amount - money
#print(f'지불 금액은 : {amount:4,d} 이고 받은 금액은 : {money:4,d} 이고 잔액은 {jan:4,d} 원 입니다.')

# 50,000 원권은 ?장, 10,000원권은 ?장,
# 5,000원권은 ?장, 1,000원권은 ?장
# 500원은 ?개, 100원은 ?개
# 50원은 ?개, 10원은 ?개 입니다.
