# csv 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv7lib.py에 작성함
# 모듈명은 sjv7로 줄여서 사용함
import sungjukv7lib as sjv7

while True:
    # 메뉴 표시 및 값 입력
    menu = sjv7.DisplayMenu()

    if menu == '1': sjv7.addSungjuk()
    elif menu == '2': sjv7.readSungjuk()
    elif menu == '3': sjv7.readOneSungjuk()
    elif menu == '4': sjv7.modifySungjuk()
    elif menu == '5': sjv7.removeSungjuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력했습니다.')