# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv5lib.py에 작성함
# 모듈명은 sjv5로 줄여서 사용함
import sungjukv5lib as sjv5


while True:
    menu = sjv5.DisplayMenu()

    if menu == '1': sjv5.addSungjuk()
    elif menu == '2': sjv5.readSungjuk()
    elif menu == '3': sjv5.readOneSungjuk()
    elif menu == '4': sjv5.modifySungjuk()
    elif menu == '5': sjv5.removeSungjuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력했습니다.')