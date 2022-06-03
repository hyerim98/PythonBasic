'''
    외장함수 : import하여 사용해야 함

    list of python modules 구글링하면 외장 함수 목록들이 나옴

    * glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
    * os : 운영체제에서 제공하는 기본 기능
    * time : 시간 관련 함수
    * datetime : 날짜 관련 함수
'''
import glob
import os
import time
import datetime

# 확장자가 py인 모든 파일
print(glob.glob("*.py"))

# 현재 디렉토리
print(os.getcwd())

folder = "sample_dir"
if os.path.exists(folder) :
    print("이미 존재하는 폴더입니다")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다")
else :
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다")

# 현재 디렉토리에 존재하는 파일들
print(os.listdir())

# 현재 시간
print(time.localtime())

# 사용자 정의로 현재 시간 출력
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 오늘 날짜
print(datetime.date.today())

# 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days = 100)
print(today + td)