# 성적 데이터를 담고있는 클래스와
# 성적 처리에 필요한 기능들로만 구성된 클래스로 나눠 작성
class SungJukVO:
    # 생성자
    def __init__(self, name, kor, eng, mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__avg = 0.0
        self.__grd = '가'

    def __str__(self):
        result = f'{self.__name} {self.__kor} {self.__eng} {self.__mat} ' \
                 f'{self.__tot} {self.__avg} {self.__grd}'
        return result

    # setter/getter
    # kor, eng, mat - getter
    # tot, avg, grd - setter/getter

    @property
    def kor(self):
        return self.__kor

    @property
    def eng(self):
        return self.__eng

    @property
    def mat(self):
        return self.__mat

    @property
    def tot(self):
        return self.__tot

    @tot.setter
    def tot(self, tot):
        self.__tot = tot

    @property
    def avg(self):
        return self.__avg

    @tot.setter
    def avg(self, avg):
        self.__avg = avg

    @property
    def grd(self):
        return self.__grd

    @tot.setter
    def grd(self, grd):
        self.__grd = grd


class SungJukService:
    @staticmethod
    def read_sungjuk(self):
        name = input('이름은 ?')
        kor = int(input('국어는 ?'))
        eng = int(input('영어는 ?'))
        mat = int(input('수학은 ?'))

        # sj =  SungJukVO(name,kor,eng,mat)
        # return sj

        return SungJukVO(name,kor,eng,mat)

    # 성적처리
    @staticmethod
    def compute_sungjuk(self, sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        if sj.avg >= 90: sj.grd = '수'
        elif sj.avg >= 80: sj.grd = '우'
        elif sj.avg >= 70: sj.grd = '미'
        elif sj.avg >= 60: sj.grd = '양'


# 성적 객체 생성
# 객체가 생성되는 것을 감춤 - 아래 코드 제거
#sj = SungJukVO('혜교', 99, 98, 97)

# static 메서드이므로 객체 생성과정없이 바로 함수 호출
# sjsrv = SungJukService()
sj = SungJukService.read_sungjuk()
SungJukService.compute_sungjuk()

print(sj)

# setter 접근 제한하기 - inspect 모듈 이용
# SungJukService 의 computeSungJuk함수에 의해서만
# tot, avg, grd를 변경하루 수 있도록 제한
sj.tot = 11  # computeSungJunk 함수 없이 개별적으로 변경 가능
