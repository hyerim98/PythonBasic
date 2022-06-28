import datetime
import time
import os
import numpy

# 현재 날짜와 시간
today = datetime.datetime.now()
print(today, type(today))


# 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜 출력
for i in range(5, 0, -1) :
    date = datetime.timedelta(days = i)
    print(today - date)


# strftime : 날짜 포맷
print(today.strftime('%H:%M:%S'))


# strptime : 문자열을 시간 타입으로 변환
str = "2020-05-04"
ret = datetime.datetime.strptime(str, '%Y-%m-%d')
print(ret, type(ret))


# 1초에 한 번씩 현재 시간을 출력
# while True :
#     today = datetime.datetime.now()
#     print(today)
#     time.sleep(1)



# 현재 디렉터리의 경로 출력
dict = os.getcwd()
print(dict, type(dict))

# 파일 이름 변경
# os.rename('./study.txt', './python.txt')


# numpy
for num in numpy.arange(0, 5, 0.1) :
    print(num)