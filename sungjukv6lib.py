# 성적프로그램 v6
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 함수를 이용한 성적처리 프로그램

# 성적 데이터 저장할 변수 선언
sjs = []

# sungjuk.dat 파일을 읽어서 sjs 변수에 초기화
def loadSungjuk():
    global sjs
    # 파일에 저장된 성적데이터들을 행단위로 읽어 리스트에 저장
    with open('data/sungjuk.dat', encoding='UTF-8') as f:
        data = f.readlines()
    print(data)

    outs = [] # 성적 데이터를 저장하기 위해 리스트 선언
    for d in data: # 리스트에 저장된 성적데이터에서 한 건씩 읽어와서
        items = d.strip().split(',') # 읽어온 데이터를 컴마로 분리하고, 불필요 문자 제거
        # dict형식으로 성적데이터를 재작성함
        item = {'name': items[0], 'kor': items[1], 'eng': items[2],
                'mat': items[3], 'tot':items[4], 'avg':items[5], 'grd':items[6] }
        # dict로 작성된 데이터를 리스트에 저장
        outs.append(item)
    sjs = outs

# 성적데이터들을 sungjuk.dat 파일에 저장
# [ {'name': 혜교, 'kor': 77, 'eng': 33, 'mat': 86},
#   {'name': 지현, 'kor': 66, 'eng': 44, 'mat': 54},
#   {'name': 수지, 'kor': 66, 'eng': 55, 'mat': 43} ]
def saveSungjuk(sjs):
    with open('data/sungjuk.dat', 'w', encoding='UTF-8') as f:
        # 방금 입력한 성적데이터와
        # 기존에 입력한 모든 성적 데이터를 파일에 함께 저장
        for sj in sjs:
            dat = f"{sj['name']},{sj['kor']},{sj['eng']},{sj['mat']},{sj['tot']},{sj['avg']},{sj['grd']}\n"
            f.write(dat)


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

    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}

    return sj

def addSungjuk():
    # 성적 데이터 입력받기
    sj = intpuSungjuk()

    # 입력받은 성적 데이터 초기화
    tot, avg, grd = computeSungjuk(sj)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    sjs.append(sj)
    print(sjs)

    # sjs 에 저장된 성적데이터를 파일에 저장
    saveSungjuk(sjs)

def readSungjuk():
    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '=============================='
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]} {sj["tot"]} {sj["avg"]} {sj["grd"]}')

    input('성적 데이터 조회 완료')

def readOneSungjuk():
    name = input('조회할 학생의 이름 : ')
    sj = None
    for item in sjs:
        if item['name'] == name: sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-----------------------------------'
    print(hdr)
    computeSungjuk(sj)
    for k in sj.keys():
        print(sj.get(k), end=' ')

    input('성적 데이터 조회 완료')

def modifySungjuk():
    name = input('수정할 학생의 이름 : ')

    idx = None
    for i in range(len(sjs)-1):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
        if sjs[i]['name'] == name:
            idx = i
            break

    # 새로운 값을 입력받음
    kor = int(input(f'새로운 국어 :  ({sjs[idx]["kor"]})'))
    eng = int(input(f'새로운 영어 :  ({sjs[idx]["eng"]})'))
    mat = int(input(f'새로운 수학 :  ({sjs[idx]["mat"]})'))

    # 다시 성적 처리
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    tot,avg,grd = computeSungjuk(sj)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    # 리스트에 다시 저장
    sjs[idx] = sj

    # 수정된 성적데이터를 파일에 저장
    saveSungjuk(sjs)


def removeSungjuk():
    name = input('삭제할 데이터의 학생 이름 : ')
    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인덱스 조사
        item = sjs[i]
        if item['name'] == name: idx = i
    sjs.pop(idx)

    # 수정된 성적데이터를 파일에 저장
    saveSungjuk(sjs)

def computeSungjuk(sj):
    tot = sj['kor'] + sj['eng'] + sj['mat']
    avg = tot / 3
    grd = '가'
    if avg >= 90: grd = '수'
    elif avg >= 80: grd = '우'
    elif avg >= 70: grd = '미'
    elif avg >= 60: grd = '양'
    return tot, avg, grd






