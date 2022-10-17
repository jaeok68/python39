# ex48) 복리계산
# 지금 현재 수지의 통장잔액이 25,000원이다. 은행이자가 연 6%라 가정할 때,
# 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을
# 아래 그림을 참고하여 작성하여라. (ComputeInvestment)
money = 25000 # 통장잔액
inter = 1.06  # 이율
limit = money * 2
year = 0
#while True:
#    if money > limit: break
#    money = money * inter
#    year += 1
for i in range(999):
    if money > limit:break
    money = money * inter

print(f'{i+1} 년 째, 잔액은 {money:,.0f}원')

# ex51) 구구단 테이블 출력
i = 2
for i in range(10):
    print('------------')
    print(f'{i} 단 출력')
    print('------------')

    for j in range(9):
        print(f'{i} * {j+1} = {i*(j+1)}')

# ex53) 입력한 연도의 1월 달력 출력
#year = int(input('년도는 : '))
year=2022
exyear31 = ((year - 1)*365 + (year-1)/4 - (year-1)/100 + (year-1)/400) % 7
# 0:일, 1:월, ..5:금, 6:토
print(int(exyear31) ) # 2021년 12월 31일의 요일
print(int(exyear31) + 1) # 2022년 1월 1일의 요일