# 성적프로그램 v8
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 함수를 이용한 성적처리 프로그램
from SungJukVO import SungJukVO
from SungJukv8DAO import SungJukv8DAO as sjdao


class SungJukv8Lib:
    @staticmethod
    def display_menu():
        main_menu = f'''
        성적 처리 프로그램 v8 '
        ----------------------'
        1. 성적 데이터 추가'
        2. 성적 데이터 조회'
        3. 성적 데이터 상세조회'
        4. 성적 데이터 수정'
        5. 성적 데이터 삭제'
        0. 프로그램 종료'
        ----------------------'''
        print(main_menu)
        menu = input('==> 메뉴를 선택하세요 : ')

        return menu

    @staticmethod
    def __input_sungjuk():
        name = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        mat = int(input('수학 : '))

        sj = [name, kor, eng, mat]

        return SungJukVO(name, kor, eng, mat)

    @staticmethod
    def add_sungjuk():
        # 성적 데이터 입력받기
        sj = SungJukv8Lib.__input_sungjuk()

        # 입력받은 성적 데이터 초기화
        SungJukv8Lib.__compute_sungjuk(sj)

        # 성적 데이터 테이블에 저장
        if sjdao.insert_sungjuk(sj) > 0:
            print('성적데이터 추가 완료!!')

    @staticmethod
    def read_sungjuk():
        hdr = '이름 국어 영어 수학\n'
        hdr += '===================='
        print(hdr)

        rows = sjdao.select_sungjuk()

        result = ''
        for row in rows:
            result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'
        print(result)

    @staticmethod
    def readone_sungjuk():
        name = input('조회할 학생의 이름 : ')

        hdr = '이름 국어 영어 수학 총점 평균 학점\n'
        hdr += '-----------------------------------'
        print(hdr)

        # 입력한 학생이름으로 성적테이블을 조회해서
        # 조회된 결과를 출력
        # 성적테이블에서 이름/국어/영어/수학만 select해서 출력
        row = sjdao.selectone_sungjuk(name)

        result = f'{row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]:.1f} {row[7]} \n'
        print(result)

    @staticmethod
    def modify_sungjuk():
        name = input('수정할 학생의 이름 : ')

        sj = sjdao.selectone_sungjuk(name)
        # 번호/이름/국어/영어/수학/총점/평균/학점/등록일


        # 새로운 값을 입력받음
        kor = int(input(f'새로운 국어 :  ({sj[1]})'))
        eng = int(input(f'새로운 영어 :  ({sj[2]})'))
        mat = int(input(f'새로운 수학 :  ({sj[3]})'))

        # 다시 성적 처리
        sj = SungJukVO(name, kor, eng, mat)
        tot,avg,grd = SungJukv8Lib.__compute_sungjuk(sj)

        cnt = sjdao.update_sungjuk(sj)

        if cnt > 0 : print('수정 성공!!')

    @staticmethod
    def remove_sungjuk():
        name = input('삭제할 데이터의 학생 이름 : ')

        cnt = sjdao.delete_sungjuk(name)

        if cnt > 0: print('삭제 성공!!')

    @staticmethod
    def __compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3

        if sj.avg >= 90: sj.grd = '수'
        elif sj.avg >= 80: sj.grd = '우'
        elif sj.avg >= 70: sj.grd = '미'
        elif sj.avg >= 60: sj.grd = '양'

