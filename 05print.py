# print 함수
# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 출력함

name = '홍길동'
kor = 99
eng = 98
mat = 99
tot = kor + eng + mat
avg = tot / 3
# 출력1
print(name)
print(kor, eng, mat)
print(tot, avg)

# 출력 2
print('이름 : ', name)
print('국어 : ', kor, '영어 : ', eng, '수학 : ', mat)
print('총점 : ', tot, '평균 : ', avg)

# 출력 3 - 출력서식 사용 : % 문자 사용
# print(출력서식 % 변수들...)
# 출력서식 문자 : %d %f %s
print('이름: %s' % name)
print('국어 : %03d, 영어 : %03d, 수학 : %03d' % (kor, eng, mat) )
print('총점 : %d, 평균 : %.1f' % (tot, avg) )

# 출력 4 - 인덱스, 출력서식 사용 : .format함수 사용
# print({인덱스:출력서식} .format(변수들...))
print('이름 : {0:s}'.format(name))
print('국어 : {:03d}, 영어 : {:03d}, 수학 : {:03d}'.format(kor, eng, mat) ) # 인덱스 생략 가능
print('총점 : {0:d}, 평균 : {1:.1f}({1:1f})'.format(tot, avg) ) # 특정 변수를 반복출력 가능
print('총점 : {1:d}, 평균 : {0:.1f}({0:1f})'.format(avg, tot) ) # 변수의 출력순서 재조정

# 출력 5 - 문자열 템플릿(f-string) : py 3.6이후 지원(추천!)
# # print(f'{변수명:출력서식}')
print(f'이름 : {name:s}')
print(f'국어 : {kor:03d}, 영어 : {eng:03d}, 수학 : {mat:03d}')
print(f'총점 : {tot:d}, 평균 : {avg:.1f}({avg:1f})' )

# % 서식
print('7 X 1 = %d' % (7 * 1) )
print('7 X 2 = %d' % (7 * 2) )
print('7 X 3 = %d' % (7 * 3) )
print('7 X 4 = %d' % (7 * 4) )
print('7 X 5 = %d' % (7 * 5) )
print('7 X 6 = %d' % (7 * 6) )
print('7 X 7 = %d' % (7 * 7) )
print('7 X 8 = %d' % (7 * 8) )
print('7 X 9 = %d' % (7 * 9) )

# .format
print('7 X 1 = {:d}'.format(7 * 1)  )
print('7 X 2 = {:d}'.format(7 * 2)  )
print('7 X 3 = {:d}'.format(7 * 3)  )
print('7 X 4 = {:d}'.format(7 * 4)  )
print('7 X 5 = {:d}'.format(7 * 5)  )
print('7 X 6 = {:d}'.format(7 * 6)  )
print('7 X 7 = {:d}'.format(7 * 7)  )
print('7 X 8 = {:d}'.format(7 * 8)  )
print('7 X 9 = {:d}'.format(7 * 9)  )


# f-string
print(f'7 X 1 = {(7 * 1):2d}'  )
print(f'7 X 2 = {(7 * 2):2d}'  )
print(f'7 X 3 = {(7 * 3):2d}'  )
print(f'7 X 4 = {(7 * 4):2d}'  )
print(f'7 X 5 = {(7 * 5):2d}'  )
print(f'7 X 6 = {(7 * 6):2d}'  )
print(f'7 X 7 = {(7 * 7):2d}'  )
print(f'7 X 8 = {(7 * 8):2d}'  )
print(f'7 X 9 = {(7 * 9):2d}'  )