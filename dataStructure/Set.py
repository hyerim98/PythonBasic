'''
    Set
        - 집합
        - 중복 안됨
        - 순서 없음
'''

my_set = {1,2,3,3,3}
print(my_set)

java = {"AAA", "BBB", "CCC"}
python = set(["AAA", "DDD"])

# java와 python을 모두 할 수 있는 사람(교집합)
print(java & python)
print(java.intersection(python))

# java나 python을 할 수 있는 사람(합집합)
print(java | python)
print(java.union(python))

# java 할 수 있지만, python은 할 줄 모르는 사람(차집합)
print(java - python)
print(java.difference(python))

# 추가
python.add("EEE")
print(python)

# 삭제
java.remove("BBB")
print(java)