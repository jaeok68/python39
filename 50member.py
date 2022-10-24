# 회원가입을 처리하는 클래스 생성
# MemberVO :
#     userid, passwd, name, email, milege, grade
# MemberService :
#  registerMember  : 회원 정보 입력
#  processMemberGrade : 마일리지에 따라 회원 등급 결정
#      vip : 마일리지 - 10000이상
#      gold : 마일리지 - 7000이상
#      silver : 마일리지 - 4000이상
#      bronze : 마일리지 - 1000이상
#      member : 그외
class MemberVO:
    def __init__(self, userid, passwd, name, email, milege):
        self.__userid = userid
        self.__passwd = passwd
        self.__name = name
        self.__email = email
        self.__milege = milege
        self.__grade = 'member'

    def __str__(self):
        result = f'{self.__userid} {self.__passwd} {self.__name} ' \
                 f'{self.__email} {self.__milege} {self.__grade}'
        return result

    # @property
    # def userid(self):
    #     return self.__userid

    # @property
    # def passwd(self):
    #     return self.__passwd
    #
    # @property
    # def name(self):
    #     return self.__name
    #
    # @property
    # def email(self):
    #     return self.__email

    @property
    def milege(self):
        return self.__milege

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade


class MemberService:
    @staticmethod
    def registerMember():
        userid = input('userid : ')
        passwd = input('passwd : ')
        name = input('name : ')
        email = input('email : ')
        milege = int(input('milege : '))

        return MemberVO(userid, passwd, name, email, milege)

    @staticmethod
    def processMemberGrade(mvo):
        if mvo.milege >= 10000: mvo.grade = 'VIP'
        elif mvo.milege >= 7000: mvo.grade = 'gold'
        elif mvo.milege >= 4000: mvo.grade = 'silver'
        elif mvo.milege >= 1000: mvo.grade = 'bronze'


# 실행
mb = MemberService.registerMember() # 회원정보 입력
MemberService.processMemberGrade(mb) # 회원등급 처리
print(mb) # => 결과 출력
