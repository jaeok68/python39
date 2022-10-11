# 수식 expresssion
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 => 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 대입식 : 대입연산자를 이용한 수식(변수 = 수식)
a = 10; b = 20; c = 30
print(a, b, c)

x, y, z = 10, 20, 30
print(x,y,z)

# 산술식 : 산술연산자(+,-,*,/)를 이용한 수식
# 파이썬에서는 //, %, ** 도 지원
print(10 / 3, 10 % 3, 10 // 3) # 나누기, 나머지, 몫
print(10**1, 10**2, 10**3) # 지수 연산

# 관계식 : 관계 연산자(대소, 순서관계)를 이용한 수식
print(10 > 3, 10 < 3)

# 논리식 : 논리 연산자(논리 합/곱/부정)를 이용한 수식
# 또한, 둘이상의 논리식이나 관계식으로 구성된 수식
# 논리식의 경우, 수식의 구성에 따라 단축식 평가(short-circuit)가 가능
print((5 == 3) and (5 > 3))
print((5 != 3) or (5 > 3))
# and 연산시 첫번째 수식의 결과가 F면 단축식평가 적용
print(3>5 and 2<3)
# or 연산시 첫번째 수식의 결과가 T면 단축식평가 적용
print(2<3 or 3<5)

# 복합 대입연산자 : 대입연산자와 산술연산자를 결합한 수식
# 보통 수식을 간단히 작성시 사용 - 축약표현
# 변수 = 변수 + 수식 => 변수 += 수식

avg = 95.6
score = 85
print('-----')
print(2<3 and 3<5, "\t", 2<3 and 3>5)
print(2<3 or 3<5, "\t", 2>3 or 3<5, "\t", 2>3 or 3>5)
print(not(2<3 and 3<5), "\t", not(2>3 or 3<5))
print(not(56<=78), "\t", avg>=80 and avg < 90)
print("python" and 9>7, "\t", 68 and 9>7)
print(9>7 or 0, "\t", 0 and 9>7)
print(9>7 and 10, "\t", 0 or 1)

# 연산자 우선순위
# 괄호내 연산자 -> 단항연산자 -> 산술연산자 -> 관계연산자 -> 논리연산자

# 연산자의 부수적인 기능 - 문자열 연산
# + : 문자열 연결
# * : 문자열 반복 연결
str1 = 'Hello'
str2 = 'World'
print(str1 + ' ' + str2)

print(str1 * 3)
print(3 * str1)

# 단, 숫자와 문자열의 + 연산시 오류발생 -> 형변환 필요
# 문자열을 숫자로 변환 : int(), float() 이용
print('123' + '456')
#print(123 + '456') # 오류 발생
print(123 + int('456'))

# 숫자형과 문자형의 논리 연산
# 0 또는 빈 문자열은 False로 인식
# bool 함수를 이용하면 지정한 값의 논리값을 알수 있음
print(bool(0), bool(''))
print(bool(1), bool('abc'))

# 다음 수식의 결과는 True인 값이 출력
print(0 and 'abc', 1 and 'abc')
print('' or 'abc', '' and 'abc')