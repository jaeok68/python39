# json 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv6lib.py에 작성함
# 모듈명은 sjv6로 줄여서 사용함
import sungjukv6blib as sjv6b

# 프로그램 시작전 데이터 초기화
# 파일에 저장된 성적데이터 불러오기
sjv6b.loadSungjuk()
while True:


    # 메뉴 표시 및 값 입력
    menu = sjv6b.DisplayMenu()

    if menu == '1': sjv6b.addSungjuk()
    elif menu == '2': sjv6b.readSungjuk()
    elif menu == '3': sjv6b.readOneSungjuk()
    elif menu == '4': sjv6b.modifySungjuk()
    elif menu == '5': sjv6b.removeSungjuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력했습니다.')