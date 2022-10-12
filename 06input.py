# input 함수
# 변수명 = input(입력메시지)

# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 출력함

#name = input('이름은 : ')
#kor = int(input('국어점수 : '))
#eng = int(input('영어점수 : '))
#mat = int(input('수학점수 : '))
#tot = kor + eng + mat
#avg = tot / 3
#print(f'이름 : {name:s}')
##print(f'국어 : {kor:d}, 영어 : {eng:d}, 수학 : {mat:d}')
#print(f'총점 : {tot:d}, 평균 : {avg:.1f}')

# p57 ex3)
# 지방,탄수화물,단백질 입력받아 총 칼로리 계산
# 풀이1
fat = 25
carbo = 520
protein = 45
totcal = fat * 9 + carbo * 4 + protein * 4
print(totcal)

# 풀이2 - input 함수 사용
#fat = int(input("지방의 그램을 입력하세요 : "))
#carbo = int(input("탄수화물의 그램을 입력하세요 : "))
#protein = int(input("단백질의 그램을 입력하세요 : "))
#totcal = fat * 9 + carbo * 4 + protein * 4
#print(f'총칼로리 : {totcal:4,d} cal')

# 성적처리 프로그램의 메뉴화면 작성 2
main_menu =  '성적 처리 프로그램 v1 \n'
main_menu += '----------------------\n'
main_menu += '1. 성적 데이터 추가\n'
main_menu += '2. 성적 데이터 조회\n'
main_menu += '3. 성적 데이터 상세조회\n'
main_menu += '4. 성적 데이터 수정\n'
main_menu += '5. 성적 데이터 삭제\n'
main_menu += '0. 프로그램 종료\n'
main_menu += '----------------------\n'
print(main_menu)

# 성적처리 프로그램의 메뉴화면 작성 2
main_menu =  f'''
성적 처리 프로그램 v1 '
----------------------'
1. 성적 데이터 추가'
2. 성적 데이터 조회'
3. 성적 데이터 상세조회'
4. 성적 데이터 수정'
5. 성적 데이터 삭제'
0. 프로그램 종료'
----------------------'''
print(main_menu)

choise = int(input('==> 작업을 선택하세요 : '))
print(f'작업 : {choise:d}')
