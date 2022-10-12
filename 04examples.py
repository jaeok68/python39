# 1
# 프로그래밍 언어 실습시 글꼴은
# 고정폭 글꼴을 사용할 것을 추천!!
print("""\
☆   ☆    ☆☆     ☆☆☆☆    ☆☆☆☆    ☆     ☆      /////
☆   ☆   ☆  ☆    ☆    ☆  ☆    ☆   ☆   ☆      | o o |
☆☆☆☆☆  ☆    ☆   ☆☆☆☆    ☆☆☆☆      ☆ ☆      (|  ∧  |)
☆   ☆  ☆☆☆☆☆☆   ☆   ☆   ☆   ☆      ☆        | [_] |
☆   ☆  ☆    ☆   ☆    ☆  ☆    ☆     ☆         -----""")

print('*   *     **')
print('*   *    *  *')
print('*****   *    *')
print('*   *   ******')
print('*   *   *    *')


print("""\
               +---+
               |   |
          +---++---+
          |   ||   |
     +---++---++---+    /\\_/\\     -----
     |   ||   ||   |   ( \' \' )   /Hello\\
+---++---++---++---+   (  _  )  < Junior|
|   ||   ||   ||   |    | | |    \\Coder!/
+---++---++---++---+   (__|__)    -----""")

# 3
# rate1, 1stPlayer, myprogram.java, long, TimeLimit, numberOfWindows
rete1 = "" ;
long=4;
TimeLimit = 1;
numberOfWindows = ""

# 4
x, y, z =1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8
print("3*x", "3*x+y", "(x+y)/7", "(3*x+y)/(z+2)")
print(3 * x, 3*x + y, (x+y)/7, ( 3 * x + y ) / ( z + 2) )

print("s = s0 + v0*t + 1/2*g*t**2")
print(s0 + v0*t + (1/2)*g*t**2)

print("G = 4*&pi**2 * (a**3)/(p**2 * (m1+m2))")

print("FV = PV * (1+INT/100)**YRS")

print("c=sqrt(a**2 + b**2 -2*a*b*cos(r))")

# 6
x, y, m, n = 2.5, 1.5, 18, 4

#가.  x + n * y - (x + n) * y
print(x + n * y - (x + n) * y)
#나.  m / n + m % n
print(m / n + m % n)
#다.  5 * x - n / 5
print(5 * x - n / 5 )
#라.  1 - (1 - (1 - (1 - (1 - n))))
print(1 - (1 - (1 - (1 - (1 - n)))))

# 7
print(3 + 4.5 * 2 + 27 / 8)
# 논리연산시 경우에 따라 단축식 펭가가 적용되기도 함
print(True or False and 3 < 4 or not (5 == 7))
print(True or 3 < 5 and 6 >= 2)

# print(not True > 'A')
print(not True > bool('A')) # not (True > True)
print(False > True)

# print(7 % 4 + 3 -2 / 6 * 'Z')
print(7 % 4 + 3 -2 / 6 * bool('Z'))

#print('D' + 1 + 'M' % 2 / 3)
print(bool('D')+1+bool('M') % 2 / 3)

print(5.0 / 3. + 3 / 3)
print(53 % 21 < 45 / 18)

print((4 < 6) or True and False or False and (2 > 3))

print(7-(3 + 8 * 6 + 3) - (2 + 5 * 2))

# 9
#가.   true && false && true || true      나. true || true && true && false
print(True and False and True or True)
print(True or True and True and False)
#다.   (true && false) || (true && ! false) || (false && !false)
print((True and False) or (True and not False) or (False and not False) )
#라.   (2 < 3) || (5 > 2) && !(4 == 4) || 9 != 4
print( (2 < 3) or (5 > 2) or not (4==4) or 9 != 4)
#마.   6 == 9 || 5 < 6 && 8 < 4 || 4 > 3
print( 6 == 9 or 5 < 6 and 8 < 4 or 4 > 3 )


# 10
#10. 다음 중 유효한 표현식을 찾고, 그 결과 값의 데이터 유형을 서술하여라.
#가.   27 / 13 + 4                           나.   27 / 13 + 4.0
print(27 / 13 + 4)
print(27 / 13 + 4.0)
#다.   42.7 % 3 + 18                           라.   (3 < 4) && 5 / 8
print(42.7 % 3 + 18)
# 논리식과 산출식(값)이 결합된 수식에서는 
# 논리식의 결과가 True 면 값이 출력
# 논리식의 결과가 False면 False가 출력
print( '라 : ', (3 < 4) or 5 / 8 )
#마.   23 / 5 + 23 / 5.0                          바.   2.0 + 'a'
print( 23 / 5 + 23 / 5.0 )
#print( 2.0 + 'a') # 문자와 정수/실수간 산술연산 불가
#사.   2 + 'a'                                    아.   'a' + 'b'
#print(2 + 'a')
print('a' + 'b')
#자.   'a' / 'b'                                    차.   'a' && ! 'b'
#print('a' / 'b')
print('a' or not 'b')
#카.   ( double ) 'a' / 'b'
#(double)'a' / 'b' # 문자는 실수로의 형변환 불가

# 11. 이름과 몸무게, 나이를 변수로 선언하고 자신의 것을 값으로 초기화하는
# 프로그램을 작성하여라 (MyInfo)
name = '홍길동'
weight = 55.5
age = 35
print('이름 :' , name, '몸무게 : ', weight, '나이 : ', age)

#12. 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라. (MyAge)
# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#        만나이(출생시 0살, 생일이 지나면 + 1)
#        연나이(현재연도 - 출생연도)
birthYear = 1990
currentYear = 2022
isPassBirth = True

age = currentYear - birthYear
print('연나이 : ', age)
print('세는나이 : ', 1+age)

# 파이썬의 if 단축식 : 참일때 값 if 조건식 else 거짓일때 값
print('만나이 : ', (age + 1) if isPassBirth else age )

#13. 구구단 중 7단을 출력하는 프로그램을 작성하여라. (GuGu7Dan)
#m = 7
#for n in range(1, 10):
#   print(f'{m} * {n} = {m*n:2d}')
#    print(m, '*', n, '=', m * n)
print('7 X 1 = ', (7 * 1))
print('7 X 2 = ', (7 * 2))
print('7 X 3 = ', (7 * 3))
print('7 X 4 = ', (7 * 4))
print('7 X 5 = ', (7 * 5))
print('7 X 6 = ', (7 * 6))
print('7 X 7 = ', (7 * 7))
print('7 X 8 = ', (7 * 8))
print('7 X 9 = ', (7 * 9))

