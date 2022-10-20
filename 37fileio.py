# 파일읽기 : 파일 내 데이터 읽어오기
# 파일객체변수 = open(경로, 모드)        # py2
# with open(경로, 모드) as 파일객체변수  # py3

# 파일모드 : 파일작업 종류
# r(읽기, 생략가능), t(텍스트파일 읽기), b(바이너리파일 읽기)

# 파일읽을때 사용가능 함수
# read    : 텍스트파일의 내용을 모두 읽음
# readline : 텍스트파일의 내용을 한줄씩 읽어옴 (반복문 사용)
# readlines : 텍스트파일의 내용을 한줄씩 모두 읽어옴

# 간단한 인사말을 파일에서 읽어오기
f = open('hello.dat')
doc = f.read() #파일의 내용을 모두 읽어 문자열로 저장
f.close()
print(doc)

# V3
with open('hello.dat') as f:
    doc2 = f.read()
print(doc2)

# 인사말이 저장된 hello2.dat 파일에서도 읽어오기
with open('hello2.dat', encoding='UTF-8') as f:
    doc2 = f.read()
print(doc2)


# 여러건의 회원정보가 저장된 파일 읽어오기1
with open('member.dat', encoding='UTF-8') as f:
    doc4 = f.read() # 모두 읽기
print(doc4)


# 여러건의 회원정보가 저장된 파일 읽어오기2
with open('member.dat', encoding='UTF-8') as f:
    doc5 = f.readlines() # 행단위로 모두 읽어 리스트로 반환
print(doc5)
for doc in doc5:
    print(doc, end='')

# 여러건의 회원정보가 저장된 파일 읽어오기3
with open('member.dat', encoding='UTF-8') as f:
    doc6 = []
    doc6 = f.readline() # 행단위로 하나씩 읽어 반환
print(doc6) # 한 건만 출력됨

# 여러건의 회원정보가 저장된 파일 읽어오기4
with open('member.dat', encoding='UTF-8') as f:
    doc7 = []
    while True:
        line = f.readline() # 파일로부터 한줄 읽어서
        if not line: break  # 읽은 내용이 없으면 반복 중지
        doc7.append( line ) # 읽은 내용이 있다면 리스트에 저장
print(doc7) # 한 건만 출력됨


# 여러건의 회원정보가 저장된 파일 읽어오기5
with open('member.dat', encoding='UTF-8') as f:
    while True:
        line = f.readline()
        if not line: break
        item = line.split('/') # 각 행의 자료를 구분자로 분리해서 리스트에 저장
        out = f'{item[0]}{item[1]}{item[2]}{item[3]}'
        print(out, end='')
print(doc7) # 한 건만 출력됨

# 학생으로부터 이름,국어,영어,수학 점수를 입력받아
# 파일에 저장하세요 (파일명 : sungjuk.dat)
# 단, 점수는 임의로, 파일에 저장하는 형식은
# "이름,국어,영어,수학" 순으로 작성함
# => 혜교,99,98,99 ( csv 형식 )
