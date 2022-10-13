# while 반복문
# 횟수와는 상관없이 조건에 따라 반복실행하는 반복문
# 즉, 조건식의 결과가 참이면 실행하고, 거짓일 경우 실행을 중단함

# 변수초기화
# while 조건식:
#    반복실행할 문장
#    증감식
# ex) 1 ~ 100 사이 정수 출력

i = 1
while i <= 100:
    print(i, end=' ')
    i += 1

# ex) 1 ~ 100 사이 정수 중 홀수만 출력
i = 1
while i <= 100:
    if i % 2 != 0: print(i, end=' ')
    i += 1

# ex) 1 ~ 100 사이 정수들의 모든 합 계산후 출력
i = 1
tot = 0
while i <= 100:
    tot += i
    i += 1
print('합계 : ', tot)

# ex) 단을 입력받아 해당 단의 구구단을 출력
dan = 9
#dan=int(input('구구단 : '))
i = 1
while i <= 9:
    print(f'{dan} * {i} = {dan * i}')
    i += 1

# p79 ex3) 3의 배수이지만 2의 배수는 아닌 정수 출력하고
# 누적합도 계산해서 출력

i = 1
tot = 0
result = ''
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        result += str(i) + ' '
        tot += i
    i += 1
print(result)
print('합계 : ', tot)

# 성적처리 프로그램의 메뉴화면 작성 2
main_menu =  f'''
성적 처리 프로그램 v1 '
----------------------'
1. 성적 데이터 추가'
2. 성적 데이터 조회'
3. 성적 데이터 상세조회'
4. 성적 데이터 수정'
5. 성적 데이터 삭제'
0. 프로그램 종료'
----------------------'''
print(main_menu)

choise = int(input('==> 작업을 선택하세요 : '))
print(f'작업 : {choise:d}')

# 무한루프
# 반복문의 조건식이 언제나 참이면
# 반복을 중단하지 않고 계속 반복을 지속하는 상황
# 단, 무한루프에서 탈출하려면 break를 이용
# while True:
#    반복실행할 문장

# 반복실행 중지 : break
# 반복 실행을 중지하고 반복문에서 나올때 사용

# ex) 1 ~ 100 사이 정수들의 모든 합 계산후 출력
# 단 무한루프와 break 이용해서 작성

i = 1
hap = 0
while True:
    if i <= 100: hap += i
    else: break
    i += 1
print(hap)

# ex) 1~10000 사이 모든 정수의 합을 출력
# 단 누적합이 15000을 넘으면 반복문 중지하고 결과 출력

i = 1
tot = 0
while True:
    if tot > 15000: break
    elif i <= 1000: tot += i
    i += 1
print('합계 : ', tot, 'i = ', i)