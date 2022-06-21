# 문자열 인덱싱 1
letters = 'python'
print(letters[0], letters[2])

# 문자열 인덱싱 2
str = "홀짝홀짝홀짝"
print(str[::2]) # [시작인덱스:끝인덱스:오프셋]




# 문자열 슬라이싱 1
license_plate = "24가 2210"
print(license_plate[4:])

# 문자열 슬라이싱 2 : 거꾸로 출력
lang = 'PYTHON'
print(lang[::-1])

# 문자열 슬라이싱 3
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])



# 공백 제거
data = "   삼성전자   "
print(data.strip()) # 전체 공백 제거

data = "034235     "
print(data.rstrip()) # 오른쪽 공백 제거




# 문자열 치환 1
phoneNum = "010-1111-2222"
print(phoneNum.replace('-', ' '))

# 문자열 치환 2
s = 'abcdfe2a354a32a'
s = s.replace('a', 'A')
print(s)




# 문자열 다루기
url = "http://sharebook.kr"
index = url.find('.')
index += 1
print(url[index:])

url_split = url.split('.')
print(url_split[1])




# 문자열 곱하기
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4)


# 문자열 -> 정수로 변환
상장주식수 = "5,969,782,550"
num = 상장주식수.replace(",", "")
num = int(num)
print(type(num))



# capitalize : 앞 문자만 대문자로 치환
str = 'hello'
print(str.capitalize())


# endswith : 문자열이 해당 문자열로 끝나는지 확인
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
print(file_name.endswith(("xlsx", "xls")))


# startswith : 문자열이 해당 문자열로 시작하는지 확인
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))



# split 메서드 사용
a = "hello world"
a = a.split(" ")
print(a[1])

ticker = "btc_krw"
ticker = ticker.split('_')
print(ticker[0])

date = "2020-05-01"
date = date.split('-')