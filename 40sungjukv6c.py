# csv 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv6lib.py에 작성함
# 모듈명은 sjv6로 줄여서 사용함
import sungjukv6clib as sjv6c

# 프로그램 시작전 데이터 초기화
# 파일에 저장된 성적데이터 불러오기
sjv6c.loadSungjuk()
while True:


    # 메뉴 표시 및 값 입력
    menu = sjv6c.DisplayMenu()

    if menu == '1': sjv6c.addSungjuk()
    elif menu == '2': sjv6c.readSungjuk()
    elif menu == '3': sjv6c.readOneSungjuk()
    elif menu == '4': sjv6c.modifySungjuk()
    elif menu == '5': sjv6c.removeSungjuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력했습니다.')