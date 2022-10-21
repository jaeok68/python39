# 파일입출력을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv6lib.py에 작성함
# 모듈명은 sjv6로 줄여서 사용함
import sungjukv6lib as sjv6

while True:
    # 파일에 저장된 성적데이터 불러오기
    sjv6.loadSungjuk()

    # 메뉴 표시 및 값 입력
    menu = sjv6.DisplayMenu()

    if menu == '1': sjv6.addSungjuk()
    elif menu == '2': sjv6.readSungjuk()
    elif menu == '3': sjv6.readOneSungjuk()
    elif menu == '4': sjv6.modifySungjuk()
    elif menu == '5': sjv6.removeSungjuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력했습니다.')