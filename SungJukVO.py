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
    def name(self):
        return self.__name

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