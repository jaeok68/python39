# 반복문
# 정해진 회수만큼 특정코드를 실행하도록 만든 문장
# 파이썬에서는  for문과 while문이 지원



# 만일, 100번 출력해야 한다면 복붙을 계속할 것인가?
# 또한, 반복시 출력하는 문구가 변경된다면? - 다시 수정
# 효율적인 반복실행을 위해서 반복문을 사용함

print('Hello, World!!')

#
print('Hello, World!!')

# for 반복변수 in range(시작값, 종료값-1, 증가값);
# 반복실행할 문장
# range함수 사용하기
# range(숫자) - 0부터 숫자-1까지의 범위
list(range(100)) # 0~(10-1) 범위

# range(시작, 끝-1) -- 시작밗부터 끝값-1 까지의 범위
# List(range(1,45+1))

# range(시작, 끝-1, 증감값)
# => 시작값부터 끝값-1의 범위에 증감값을 포함
list(range(1, 10, 2))

list(range(0, 10, 2))

# ex) 1 ~ 100 사이 정수 출력
list(range(1, 100+1))

for i in range(1, 100+1):
    print(i, end=', ')

# print함수로 값 출력시 줄바꿈문자가 자동 추가됨
# 줄바꿈 문자 대신 다른 문자로 대신하려면 end속성 사용

# ex) 100 ~ 1 사이 정수 출력
for i in range(100, 0, -1):
    print(i, end=' ')

# ex) 1 ~ 100 사이 정수 중 짝수만 출력
list(range(2,100+1,2))

for i in range(2, 100+1, 2):
    print(i, end=' ')

list(range(1,100+1))
for i in range(1, 100+1):
    if i % 2 == 0: print(i, end=' ')

#ex) 1 ~ 100 사이 정수들의 모든 합 계산
hap = 0
for i in range(1, 100+1):
    hap += i
print('합계 : ', hap)

# 가우스 덧셈 공식을 이용해서
# 1 ~ 100사이 모든 정수들의 합 계산후 출력
# x ~ y 까지의 숫자를 더한 합을 구하는 공식
# ( ( x + y ) * ( y -x + 1 ) ) / 2
#n = 100
#gaussSum = n * (n + 1) // 2 #가우스 공식
#print(gaussSum)

((1+100) * (100 - 1 + 1)) / 2

# 문자열에 반복문 적용하기
# => 문자열에서 문자를 하나씩 가져와서 출력함
for i in 'Hello, World!!':
    print(i, end=' ')

# ex)  단을 입력받아 해당 단의 구구단을 출력
dan = int(input('구구단 입력 : '))
for i in range(1, 9+1):
    print(f'{dan} * {i} = {dan * i}' )

# p79 ex3)
# 1 ~ 100사이에서 3의 배수이면서 2의 배수가 아닌수를 한 줄에 출력하고
# 누적합을 출력
tot = 0
result = ''
#for i in range(3, 100+1, 3):
#    if i % 2 != 0:
#        tot += i
#        print(i, end=' ')
#print(f'합계 : {tot}')
for i in range(1, 100+1):
    if i % 3 == 0 and i % 2 != 0:
        result += str(i) + ' '
        tot += i
print(result)
print('합계 : ', tot)
