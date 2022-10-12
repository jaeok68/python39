# 20

# 22
#number 변수에 30과 35가 입력된다고 가정할 때
#각각의 if문의 결과는 무엇인가요?
number = 30
if number % 2 == 0:
    print(number , " is even." )
    print(number , " is odd." )

number = 35
if number % 2 == 0:
    print( number , " is even.")
else:
    print( number , " is odd." )

# 26 - 연봉/결혼 여부 세금 계산(0:미혼)
# 사용자가 연봉과 결혼 여부를 입력하면 다음의 세금율에 의해 납부해야
# 할 세금을 계산하는 프로그램을 작성하세요 (Tax)
# 가. 미혼인 경우 : 연봉 3000미만 - 10%,  연봉 3000이상 - 25%
# 나. 결혼한 경우 : 연봉 6000미만 - 15%,  연봉 6000이상 - 35%
salary = int(input('연봉입력 : '))
isMarried = int(input('결혼여부(0:미혼,1:기혼) : '))
tax = 0

if isMarried == 1:
    if salary < 6000: tax = salary * 0.15
    else: tax = salary * 0.35
else:
    if salary < 3000: tax = salary * 0.1
    else: tax = salary * 0.25

print(salary, isMarried, tax)

# 27 - 윤년 여부
# 2020, 2008, 2000 윤년
# 2022, 1900, 2010 평년
# 27. 다음 조건을 이용해서 현재 연도를 입력하면 윤년 여부를
# 출력하는 프로그램을 작성하세요. (LeapYear)
# 가. 현재 연도가 4로 나눠 떨어지지만, 100으로는 나눠 떨어지지 않음
# 나. 현재 연도가 400으로 나눠 떨어짐
year = int(input('연도 입력 : '))
if ( (year % 4 == 0) and (year % 100 != 0) ) or (year % 400 == 0):
    print('윤년입니다')
else:
    print('평년입니다')



# 25 - 복권 발행 프로그램25. 다음 조건을 만족하는 복권 발행 프로그램을 작성하세요. (Lotto)
# 가. 사용자로부터 복권 숫자 3자리를 입력 받으세요 (yourkey)
# 나. 변수에 임의의 복권 숫자 3자리를 초기화합니다 (lottokey)
# 다. 사용자가 입력한 복권 숫자가 모두 일치 : 상금 1백만 지급
# 라. 일치하지 않는 경우 : “아쉽지만, 다음 기회를!” 라고 출력

import random
yourkey = int(input('복권 숫자 3자리 입력 : '))
lottokey = 111
if yourkey == lottokey:
    print('상금 100만~')
else:
    print('아쉽지만, 다음 기회를!')