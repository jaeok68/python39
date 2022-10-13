# 다중 if문
# if~else만으로 다양한 조건을 판단하기 어려움
# => 물론 여러개의 if문을 사용해서 처리 가능하기도 함
# 다양한 조건에 따라 판단하기 위해서는
# if ~ elif ~ else 구문을 사용해야 함

# if 조건식1:
#    조건식1이 참일때 실행할 문장
# elif 조건식2:
#    조건식2이 참일때 실행할 문장
# ...
# else:
#    거짓일때 실행할 문장

# 결과 조건 : 점수 0 ~ 50 => 노력하세요
#             51 ~ 80  => 잘했어요
#             81 ~ 100 => 최고예요!
jumsu = 55
#if jumsu <= 50:
#    print('노력하세요')
#if jumsu <= 80: print('잘했어요')
#if jumsu <= 100: print('최고예요')
# => 결과가 올바르지 않게 나옴
if 0 <= jumsu <= 50:
    print('노력하세요')
if 51 <= jumsu <= 80: print('잘했어요')
if 81 <= jumsu <= 100: print('최고예요')

if jumsu <= 50: 
    print('노력하세요')
else:
    if jumsu <= 80: 
        print('잘했어요')
    else:
        if jumsu <= 100: 
            print('최고예요')
# 들여쓰기를 조건에 따라 작성해야 함 - 가독성 떨어짐
if jumsu <= 50:
    print('노력하세요')
elif jumsu <= 80:
    print('잘했어요')
elif jumsu <= 100:
    print('최고예요')
# 조건문장 작성시 들여쓰기를 일정하게 사용 - 가독성 좋음    


# 성적처리 프로그램 v3
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 출력함
# 학점처리 조건은 수우미양가로 함
name = input('이름은 : ')
kor = int(input('국어점수 : '))
eng = int(input('영어점수 : '))
mat = int(input('수학점수 : '))
tot = kor + eng + mat
avg = tot / 3
grd = '가'
if avg >= 90: grd = '수'
elif avg >= 80: grd = '우'
elif avg >= 70: grd = '미'
elif avg >= 60: grd = '양'
print(f'이름 : {name} 국어 : {kor} 영어: {eng} 수학 : {mat}')
print(f'총점 : {tot} 평균 : {avg:.1f} 학점 : {grd}')

# ex) p77 항공사 짐 무게 측정
cargo = int(input('짐의 무게(단위Kg) : ') )
result = '수수료가 없습니다'
if cargo >= 10:
    result = '수수료는 10,000원입니다'
print(f'짐의 무게는 {cargo}kg이고 {result}' )


# ex) p77 항공사 짐 무게에 따른 수수료 계산
cargo = int(input('짐의 무게(단위Kg) : ') )
result = '수수료가 없습니다'
pay = 0
if cargo >= 10:
    pay = (cargo // 10) * 10000
    result = f'수수료는 {pay}입니다'
print(f'짐의 무게는 {cargo}kg이고 {result}' )

# 출생연도를 입력받아 나이 계산한 후
# 나이에 따른 학생 분류 후 결과 출력
# 8 ~ : 초등학생
# 14 ~ : 중학생
# 17 ~ : 고등학생
# 20 ~ : 대학생
# 26 ~ : 학생이 아닙니다.

#import datetime

byear = int(input('출생년도 입력 : '))
#Year = datetime.datetime.now().year
Year = 2022
age = Year - byear + 1
result = '학생이 아닙니다'
if age >= 26:
    result = '학생이 아닙니다'
elif age >= 20:    
    result = '대학생입니다'
elif age >= 17:    
    result = '고등학생입니다'
elif age >= 14:    
    result = '중학생입니다'
elif age >= 8:
    result = '초등학생입니다'

print(result)


