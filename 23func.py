# 함수function
# 주어진 입력값으로 무언가를 수행하고 결과물을 내놓는 객체
# 한번 작성해두면 언제든 재사용 가능
# 논리적인 단위 분할 가능 -> 개발의 분업화
# 코드의 구현을 외부로 부터 숨길수 있음 -> 캡슐화

# 함수 정의
# def 함수이름(매개변수):
#     함수몸체

# 함수 호출
# 함수이름(인수)

# 인사말 출력하는 코드1
print('Hello, world!!')

# 인사말 출력하는 코드1 - 3번 반복

for i in range(3):
    print('Hello, world!!')
    
# 인사말 출력하는 코드3
# -> 3번 반복하는 코드를 3번 반복
# 복붙으로 해결할 수 있지만, 수정사항 생기면
# 유지보수 힘듬
for j in range(3):
    print('Hello, world!!')

# 인사말 출력하는 코드4 - 함수
def sayHello():
    for _ in range(3):
        print('Hello, world!!')

sayHello() # 함수호출


# 매개변수parameter vs 인수argument
# 매개변수 : 함수 정의시 입력으로 전달된 값을 받는 변수
# 인수 : 함수 호출시 실제 입력으로 전달하는 값
def sayHello(msg):
    for _ in range(3):
        print(f'Hello, {msg}!!')

sayHello('Python')        
# 함수 호출시 함수내부로 전달하는 실제값

sayHello('Python')
# Python : 함수호출시 함수내부로 전달하는 실제값

sayHello('Java')

# ex) 두 수를 입력받아 add라는 함수로 호출해서 결과 출력
# 단, add라는 함수는 두 입력값을 더한후 결과 출력함.
def addNums(a, b):
    print(f'{a} + {b} = {a + b}')

a = int(input('첫번째 숫자 : '))
b = int(input('두번째 숫자 : '))

addNums(a, b)

# 함수 다중정의 - overloading
# 동일한 이름의 함수를 매개변수에 따라 다른 기능으로
# 동작하도록 작성하는 것을 의미
# 파이썬에서 공식적으로 지원하는 기능은 아님 - 구현은 가능
# 다중정의를 너무 남발하면 코드가 복잡해짐

# ex) 잔돈계산하는 프로그램을 함수로 작성
# 함수명 : computeCharge(비용, 지불금액)

def computeCharge(cost, money):
    money = cost - money
    charge = money - cost  # 37660

    # 결과 출력
    print(f'''
    지불금액은 {cost:,d}원 이고,
    받은 금액은 {money:,d}원 이고
    잔액은 {charge:,d}원 입니다.
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

cost = int(input('지불 금액 : '))
money = int(input('받은 금액 : '))

computeCharge(cost, money)

# ex) - 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 : checkCredit(코드)
# dict 자료구조를 이용해서 작성
def checkCredit(code):
    cards = {'356317':'NH농협JCB카드', '356901':'신한JCB카드', '356912':'KB국민JCB카드',
            '404825': '비씨Visa카드', '438676': '신한Visa카드', '457973': '국민은행Visa카드',
            '515594': '신한마스타카드', '524353': '외환마스타카드', '540926': '국민은행마스타카드'}
    cardname = cards.get(code)
    if cardname == None: print('카드번호를 잘못 입력')
    else: print(cardname)

code = input('조회할 카드 번호 : ')
checkCredit(code)

# ex) 60갑자를 춣력해주는 프로그램을 함수로 작성
# 함수명 : checkChinaZodiac(년도)

# ex) 년도를 입력하면 십간과 십이지를 이용해서
# 해당년도의 60갑자(간지) 출력
# 십간 : 갑을병정무기경신임계
# => (10일마다 바뀌는 태양에 부쳐진 이름)
# 십이지 : 자축인묘진사오미신유술해
def checkChinaZodiac( year ):
    BASE = 1444
    ten = ('갑', '을', '병', '정', '무', '기', '경', '신', '임', '계')
    twelve = ('자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해')
    animal = ('쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지')
    i1 = ( year - BASE ) % 10
    i2 = ( year - BASE ) % 12
    print(f'{year}년은 {ten[i1]+twelve[i2]}년({animal[i2]}의 해)입니다.')

year = int(input('연도 입력 : '))
checkChinaZodiac( year )




