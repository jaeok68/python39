# 성적프로그램 v6c
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 함수를 이용한 성적처리 프로그램
import csv

# 성적 데이터 저장할 변수 선언
sjs = []

# sungjuk.dat 파일을 읽어서 sjs 변수에 초기화
def loadSungjuk():
    global sjs
    
    # 파일에 저장된 성적데이터들을 모두 읽어 리스트에 저장
    try:
        with open('data/sungjukv6c.dat', encoding='UTF-8') as f:
            data = csv.reader(f)
            sjs = list(data)
    except:
        pass

# 성적데이터들을 sungjukv6c.dat 파일에 저장
# [ [혜교, 77, 33, 86],
#   [지현, 66, 44, 54],
#   [수지, 66, 55, 43] ]
def saveSungjuk(sjs):
    # newline : 줄바꿈이 2번 추가되는 것을 제외
    with open('data/sungjukv6c.dat', 'w', encoding='UTF-8', newline='') as f:
        # 방금 입력한 성적데이터와
        # 기존에 입력한 모든 성적 데이터를 csv 형식으로 파일에 함께 저장
        wf = csv.writer(f) # csv 작업 초기화
        for sj in sjs:
            wf.writerow(sj)           # sjs 리스트의 요소를 csv 행으로 저장

# 함수 정의부
def DisplayMenu():
    main_menu = f'''
    성적 처리 프로그램 v6 '
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

def intpuSungjuk():
    name = input('이름 : ')
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    mat = int(input('수학 : '))

   # sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    sj = [name, kor, eng, mat]

    return sj

def addSungjuk():
    # 성적 데이터 입력받기
    sj = intpuSungjuk()

    # 입력받은 성적 데이터 초기화
    tot, avg, grd = computeSungjuk(sj)

    # sj['tot'] = tot; sj['avg'] = avg; sj['grd'] = grd
    # + : 2개의 리스트를 하나로 합쳐 하나의 리스트로 만듬
    sj = sj + [tot, avg, grd]

    sjs.append(sj)
    print(sjs)

    # sjs 에 저장된 성적데이터를 파일에 저장
    saveSungjuk(sjs)

def readSungjuk():
    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '=============================='
    print(hdr)

    for sj in sjs:
        print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]}')

    input('성적 데이터 조회 완료')

def readOneSungjuk():
    name = input('조회할 학생의 이름 : ')
    sj = None
    for item in sjs:
        if item['name'] == name: sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-----------------------------------'
    print(hdr)

    print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]} {sj[4]} {sj[5]:.1f} {sj[6]}')

    input('성적 데이터 조회 완료')

def modifySungjuk():
    name = input('수정할 학생의 이름 : ')

    idx = None
    for i in range(len(sjs)):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
        if sjs[i][0] == name:
            idx = i
            break

    # 새로운 값을 입력받음
    kor = int(input(f'새로운 국어 :  ({sjs[idx][1]})'))
    eng = int(input(f'새로운 영어 :  ({sjs[idx][2]})'))
    mat = int(input(f'새로운 수학 :  ({sjs[idx][3]})'))

    # 다시 성적 처리
    sj = [name, kor, eng, mat]
    tot,avg,grd = computeSungjuk(sj)
    sj = sj + [tot, avg, grd]

    # 리스트에 다시 저장
    sjs[idx] = sj

    # 수정된 성적데이터를 파일에 저장
    saveSungjuk(sjs)


def removeSungjuk():
    name = input('삭제할 데이터의 학생 이름 : ')

    idx = None
    for sj in sjs:  # 삭제할 데이터가 sjs에 있는지 조사
        if sj[0] == name:   # 만일 존재한다면
            sjs.remove(sj)  # 바로 데이터 삭제

            # 수정된 성적데이터를 파일에 저장
            saveSungjuk(sjs)

def computeSungjuk(sj):
    tot = sj[1] + sj[2] + sj[3]
    avg = tot / 3
    grd = '가'
    if avg >= 90: grd = '수'
    elif avg >= 80: grd = '우'
    elif avg >= 70: grd = '미'
    elif avg >= 60: grd = '양'

    return tot, avg, grd






