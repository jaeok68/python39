# 33. 임의의 숫자 6자리를 입력하면 신용카드의 종류와 은행정보를
# 출력하는 프로그램을 작성해보세요.  (CardCheck)
# 35(JCB카드)
# 356317 - NH농협카드, 356901 - 신한카드, 356912 - KB국민카드
# 4(비자카드)
# 404825 – 비씨카드, 438676 – 신한카드, 457973 – 국민은행
# 5(마스타카드, Maestro)
# 515594 – 신한카드, 524353 - 외환카드, 540926 – 국민은행
card = '404825'
#card = input('신용카드번호 입력(6자리) : '
result = ''
bank = ''

if card[:2] == '35':
    nums = card[2:] # 나머지 카드 번호 추출
    if nums == '6317': result = 'NH농협 JCB카드'
    elif nums == '6901': result = '신한 JCB카드'
    elif nums == '6912': result = 'KB국민 JCB카드'
    else: result = '잘못된 카드번호입니다.'
elif card[:1] == '4':
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '04825': result = 'BC 비자카드'
    elif nums == '38676': result = '신한 비자카드'
    elif nums == '57973': result = 'KB국민 비자카드'
    else: result = '잘못된 카드번호입니다.'
elif card[:1] == '5':
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '15594': result = '신한 마스타카드'
    elif nums == '24353': result = '외환 마스타카드'
    elif nums == '40926': result = 'KB국민 마스타카드'
    else: result = '잘못된 카드번호입니다.'
else: result = '잘못된 카드번호입니다.'

print(result)


# 35. 시간때를 의미하는 영어단어를 변수 daytime으로 입력받으면,
# 그에 따른 의미를 출력하는 프로그램을 작성하라 (CheckDayTime)
# morning hours                 아침시간 (7-12)
# midday / noon                 점심시간 (12-1)
# afternoon hours               오후 (1-6)
# evening hours                  저녁시간 (6-9)
# night hours                  밤시간 (9-12)
# midnight                  자정시간 (12)
# early morning hours          새벽시간 (12-5)
# small hours                 새벽 (1-3)
# dawn / daybreak         해뜰력 (5-7)
daytime = 'morning hours'
#daytime = input('시간때를 의미하는 영단어는 : ')
result = '잘못 입력하셨습니다'

if daytime == 'morning hours': result = '아침시간 (7-12)'
elif daytime in ('midday',  'noon'): result = '점심시간 (12-1)'
elif daytime == 'afternoon hours': result = '오후 (1-6)'
elif daytime == 'evening hours': result = '저녁시간 (6-9)'
elif daytime == 'night hours': result = '밤시간 (9-12)'
elif daytime == 'midnight': result = '자정시간 (12)'
elif daytime == 'early morning hours': result = '새벽시간 (12-5)'
elif daytime == 'small hours': result = '새벽 (1-3)'
elif daytime in ('dawn',  'daybreak'): result = '해뜰력 (5-7)'
print(result)

# switch ~ case 와 비슷하게 작성해보기
# 파이썬은 지금까지(~v3.9) switch ~ case 구문을 지원하지 않음
# 만일, switch ~ case 구문을 구현하려면 dict를 이용해야 함
# 한편, v3.10 이상부터는 match case 라는 구문으로 구현가능

# dict 자료구조
# 키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류임
# 객체명 = {키 : 값} => 객체명.get(키), 객체명[키]

cards = {'356317':'NH농협 JCB카드',
         '404825':'비씨 Visa카드',
         '515594':'신한 Master카드'}

print(cards.get('404825'))


daytimes = {'morning hours':'아침시간 (7-12)',
            'midday':'점심시간 (12-1)',
            'noon':'점심시간 (12-1)',
            'afternoon hours':'오후 (1-6)'}
print(daytimes.get('midday'))


# 성적처리 프로그램 v3b
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 출력함
# 학점처리 조건은 수우미양가로 함
# 학점은 dict를 이용해서 처리함

name = input('이름 : ')
kor = int(input('국어 : '))
eng = int(input('영어 : '))
mat = int(input('수학 : '))

tot = kor + eng + mat
avg = tot / 3
grds = {10 : '수', 9 : '수', 8 : '우', 7 : '미', 6 : '양'}
grade = grds.get(avg // 10)
print(f'''\
이름:{name:s}\n국어:{kor:3d}점, 영어:{eng:3d}점, 수학:{mat:3d}점
총점:{tot:3d}점, 평균:{avg:.1f}점, 학점은 {grade:s}입니다.''')

# 3항 연산자 - if 단축문 : 컴프리헨션
# 참일때 값 if 조건식 else 거짓일때 값
print('참' if True else '거짓')
print('참' if False else '거짓')

# ex) 윤년여부를 출력하는 프로그램을 작성하세요
# 단, 3항 연산자를 이용해서 구현함
year = '2012'
isLeapYear =  (year % 4 == 0 and year % 100 != 0)  or year % 400 == 0
result = '윤년입니다' if isLeapYear else '평년입니다'
print(year, result)

# ex) 년도와 월을 입력받아 윤년여부와
# 입력한 달의 마지막 날을 출력하는 프로그램을 작성하세요
# 30 : 4, 6, 9, 11
# 31 : 1, 3, 5, 8, 10, 12
# 28 : 2 (평년)
# 29 : 2 (윤년)

