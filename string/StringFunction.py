python = "Python is Amazing"

# 소문자
print(python.lower())
# 대문자
print(python.upper())
print(python[0].isupper()) # 대문자인지 확인

# 문자열 길이
print(len(python))

# 문자열 교체
print(python.replace("Python", "Java"))

# 해당 문자 몇번째의 인덱스에 있는지 확인
index = python.index("n")
print(index)
# 찾은 인덱스 이후부터 또 다른 n 문자가 있는지 확인
index = python.index("n", index + 1)
print(index)

# 문자열 찾기(없으면 -1 반환)
print(python.find("Java"))
print(python.find("Python"))

# 문자 개수
print(python.count("n"))