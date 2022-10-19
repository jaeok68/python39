# 함수 고급기능 - 키워드 인수
# 함수 호출시 전달되는 값이
# 어떤 매개변수에 지정되는지 결정 : 순서대로 할당
# 인수의 순서를 바꿔 함수를 호출할 수 있음
def addv1(a, b):
    print(f'{a} + {b} = {a + b}')

addv1(3, 5)
addv1(a=3, b=5) # 인수가 전달될 매개변수명 지정
addv1(b=3, a=5) # 매개변수 순서 바꿔 호출

# 함수 고급기능 - 디폴트 인수
# 함수 호출시 전달하는 값이 없을 경우
# 미리 설정해둔 값이 매개변수로 전달되도록 설정
def addv2(a=4, b=6):
    print(f'{a} + {b} = {a + b}')

addv2(10,10)
addv2(10)     # b매개변수에 미리 정해둔 6이 전달됨
addv2()       # a,b매개변수에 미리 정해둔 4,6이 전달됨
addv2(b=10)   # a매개변수에 미리 정해둔 4가 전달됨

# 함수 고급기능 - 가변인수
# 함수 정의시 매개변수의 갯수를 고정이 아닌 가변으로 설정
# 가변인수 선언시 args에 *라는 기호 사용
def addv3(a=7, b=9, *args):
    print(f'{a} + {b} + {args}= {a + b + sum(args)} ')

addv3()
addv3(3, 5)
addv3(3, 5, 7, 9)