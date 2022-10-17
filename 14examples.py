# p78 ex2) 숫자 맞추기
import random as rnd

print('>> 숫자 맞추기 게임 <<')
magic = rnd.randint(1, 10) # 1-10 사이 난수 정수 발생
print('magic :', magic)
while True:
    key = int(input('예상 숫자를 입력하시요 : ')) # 숫자 입력
    if magic == key:
        print('~~ 성공 ~~')
        break
    elif magic < key: print('숫자가 커요')
    else: print('숫자가 작아요')


# ex30) 숫자 맞추기 (1~100)
# 사용자로부터 1 - 100사이의 숫자를 입력 (num1)
# 변수에 임의의 숫자 3자리를 초기화합니다 (num2)
#  num1이 num2보다 크면 “추측한 숫자가 큽니다”라고 출력하세요
#  num1이 num2보다 작으면 “추측한 숫자가 작습니다”라고 출력하세요
#  num1과 num2가 같으면 “빙고! 숫자를 맞췄습니다”라고 출력하고 종료
import random

num2 = random.randint(1, 100) # 1-100 사이 난수 정수 발생
print('num2 : ', num2)
while True:
    num1 = int(input('숫자를 입력 : '))
    if num1 > num2: print('추측한 숫자가 큽니다')
    elif num1 < num2: print('추측한 숫자가 작습니다')
    else:
        print('빙고! 숫자를 맞췄습니다')
        break


# ex25) 복권 프로그램 - 3자리수 난수 생성/사용자 입력
# 난수 범위 - 100 ~ 999, 위치는 상관없이 숫자만 일치여부 판단
# ex) 123 -> 345(1), 317(2), 312(3)
# 문자열 슬라이싱을 위한 문자열 str 함수 사용
# 3개 일치 - 상금 백만원!
# 2개 일치 - 상금 5만원
# 1개 일치 - 상금 1천원
# 0개 일치 - 다음 기회에!

import random as rnd

lotto = str(rnd.randint(100, 999)) # 100-999 사이 난수 정수 발생
print('lotto : ', lotto)
# lotto1 = str(rnd.randint(1, 9))
# lotto2 = str(rnd.randint(1, 9))
# lotto3 = str(rnd.randint(1, 9))
# lotto = lotto1 + lotto2 + lotto3
mykey = str(input('3자리 복권번호 입력(100-999) : '))
match = 0
# 첫째 자리 비교
#if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
#    match += 1

# 둘째 자리 비교
#if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] == mykey[2]:
#    match += 1

# 세째 자리 비교
#if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] == mykey[2]:
#    match += 1
# 개선된 코드1
#for i in range(3):
#    lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[i] == mykey[2]
#    match += 1
# 개선된 코드2
for i in range(3):
    for j in range(3):
        if lotto[i] == mykey[j] : match += 1

# 당첨 여부 판단
if match == 3: print('당첨! 상금 백만원!!')
elif match == 2: print('당첨! 상금 만원!!')
elif match == 1: print('당첨! 상금 천원!!')
else: print('꽝! 아쉽지만 다음 기회에!')

print(lotto, mykey, match)



