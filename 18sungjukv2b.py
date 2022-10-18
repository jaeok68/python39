# 성적프로그램 v2b
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함
# 변수 선언/초기화
# 2차원 리스트를 이용한 성적처리 프로그램

# 성적 데이터 저장할 변수 선언
sjs = []

# 프로그램 메뉴 출력을 위한 변수 선언
main_menu =  f'''
성적 처리 프로그램 v2b '
----------------------'
1. 성적 데이터 추가'
2. 성적 데이터 조회'
3. 성적 데이터 상세조회'
4. 성적 데이터 수정'
5. 성적 데이터 삭제'
0. 프로그램 종료'
----------------------'''


# 프로그램 주 실행부
while True:
    print(main_menu)
    menu = input('==> 메뉴를 선택하세요 : ')
    if menu == '0':
        print('성적 프로그램을 종료합니다.!')
        break
    elif menu == '1': # 성적데이타 입력, 성적처리
        name = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        mat = int(input('수학 : '))

        tot = kor + eng + mat
        avg = tot / 3
        grd = '가'
        if avg >= 90: grd = '수'
        elif avg >= 80: grd = '우'
        elif avg >= 70: grd = '미'
        elif avg >= 60: grd = '양'

        sj = []
        sj.append(name)
        sj.append(kor)
        sj.append(eng)
        sj.append(mat)
        sj.append(tot)
        sj.append(grd)

        sjs.append(sj)

        input('성적 데이터 추가 완료')
    elif menu == '2': # 이름, 국어, 영어, 수학만 출력
        hdr = '이름 국어 영어 수학\n'
        hdr += '==================='
        print(hdr)

        for sj in sjs:
            print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]}')
 #           for s in sj:
 #               print(f'{s}', end=' ')
 #           print()

        input('성적 데이터 조회 완료')
    elif menu == '3':
        name = input('조회할 이름 : ')
        for i in range(len(names)):
            if name == names[i]:
                print(f'{names[i]},{kors[i]},{engs[i]},{mats[i]}, {grds[i]}')

        input('성적 데이터 상세조회 완료')
    elif menu == '4':
        input('성적 데이터 수정 완료')
    elif menu == '5':
        input('성적 데이터 삭제 완료')
    else: print('잘못된 번호를 입력했습니다.')