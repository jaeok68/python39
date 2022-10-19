# 내장함수
# don't reinvent the wheel
# 파이썬에서 활용빈도 높은 기능을 함수로 미리 작성해 둠
# 이러한 함수를 사용할때는 특별한 지시문 필요 X

# 숫자관련
abs(-10) # 절대값
print(abs(-10))

sum([10, 20, 30]) # 요소의 총합 계산

max([10,20,30]) # 최대값 출력
max([10,20,30]) # 최소값 출력

round(34.56) # 반올림

round(34.46) # 반올림

# 자료형 관련
type(10)
type(10.5)
type(True)

# 변환함수
ord('A') # 유니코드 문자를 입력하면 코드값 출력
print(ord('A'))

chr(65) # 코드값을 입력하면 유니콤 문자 출력

# 정렬함수
nums = [10, 7, 15, 4]
sorted(nums) # 오름차순 정렬
print(sorted(nums))

list(reversed(nums)) # 내림차수 정렬
list(reversed(nums)) # 순서반전


# 묶음 변수  = zip
names = ['혜교','지현','수지']
ages = [33, 66, 77]

actor = list(zip(names, ages))
print(actor)

# 함수를 조건식에 적용 - filter, map
# ex) 1~100사이 정수 중 짝수만 골라서 리스트에 저장
def chkEven(num):
    return num % 2 == 0

evens = []
for num in range(1, 100+1):
    if chkEven(num):
        evens.append(num)
print(evens)

# 짝수 판별하는 함수를 filter 함수로 재적용
# filter(적용할 함수, 함수에 사용할 값객체)
evens1 = list(filter(chkEven, range(1, 100+1)))
print(evens1)

# 짝수 판별하는 함수를 람다식으로 재적용
evens2 = list(filter(lambda x:x % 2 == 0, range(1, 100+1)))
print(evens2)

# ex2) 1~10 사이 정수를 제곱해서 리스트에 저장 : 생산
squares = []
for num in range(1, 10+1):
    val = num ** 2
    squares.append(val)
print(squares)

# 정수 제곱하는 함수를 만들어 재적용
def squrNum(num):
    return num ** 2

squares = []
for num in range(1, 10+1):
    squares.append(squrNum(num))
print(squares)

# 정수를 제곱하는 함수를 map 함수로 재적용
# map(적용할 함수, 함수에 적용할 대상)
# 리턴값 : 함수를 적용한 값
sqr1 = list(map(squrNum, range(1, 10+1)))
print(sqr1)

# 정수를 제곱하는 함수를 람다식으로 재적용
sqr2 = list(map(lambda x:x ** 2, range(1, 10+1)))
print(sqr2)

# 열거형 데이터 다루기 : enumerate
# 순서있는 객체들을 다룰떄 인덱스를 포함시켜 객체를 리턴해 줌
print(names) # 값만 출력

for n in names: # 값만 출력
    print(n)

idx = 0
for n in names:
    print(idx, n)
    idx += 1

for idx, name in enumerate(names): # 값과 순서 출력
    print(idx, name)


# 사용자로부터 소문자를 입력 받아 대문자로 출력하는 프로그램을 작성해보세요. 
# 단, 소문자 이외의 숫자나 문자를 입력 받으면 “잘못 입력하셨습니다!!”라는 메시지를 출력하도록 합니다. (UpperCase)
# 문자 입력 시 System.in.read() 사용
# A의 유니코드 값 : 65,      a의 유니코드 값 : 97 (  차이 : 32 )
# ex) 사용자로부터 소문자를 입력받아 대문자로 변환
# 단, 숫자나 대문자 입력시 경고 출력

#변환 알고리즘 파악
# ord('x')
# chr( ord('x') - 32 )

# 코드 구현
while True:
    ch = input('변환할 소문자 : ')

    # 입력한 문자가 소문자인지 확인
    if 97 <= ord(ch) <= 122:
        nch = chr(ord(ch) - 32)
        print(f'입력한 {ch}의 대문자는 {nch}입니다')
    elif ch == '!': break
    else:
        print('입력한 문자가 소문자가 아닙니다')

while True:
    char1 = input('소문자 입력 : ')
    if char1.islower():
        result = char1.upper()
        print(result)
        break
    else:
        print('잘못 입력')

