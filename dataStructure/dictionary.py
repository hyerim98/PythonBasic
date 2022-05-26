# Key : Value

cabinet = {3 : "A", 100 : "B"}

# 출력1
print(cabinet[3])
print(cabinet[100])
# 출력2
print(cabinet.get(3))
# 없는 key 값 호출
print(cabinet.get(5, "사물함 비어있음")) # 문자열 대신 출력

# in : 값이 있는지 없는지 확인
print(3 in cabinet)
print(5 in cabinet)

# key는 문자열도 가능
cabinet = {"A-3" : "AAA", "B-100" : "BBB"}
print(cabinet["A-3"])
print(cabinet)

cabinet["c-50"] = "CCC"
cabinet["A-3"] = "AAAAA"
print(cabinet)

# key 삭제
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# values들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# clear : 비우기
cabinet.clear()
print(cabinet)