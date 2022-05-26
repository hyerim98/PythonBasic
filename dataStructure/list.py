subway = [10, 20, 30]
print(subway)

subway = ["A", "B", "C"]
print(subway)

# index : "B"의 위치
print(subway.index("B"))

# append : 리스트에 값 추가
subway.append("D")
print(subway)

# insert : 사이에 값 추가
subway.insert(1, "E")
print(subway)

# pop : 뒤에서부터 하나씩 꺼냄
print(subway.pop())
print(subway)

# count : 같은 문자가 몇개 있는지 확인
subway.append("E")
print(subway)
print(subway.count("E"))

# sort : 정렬
num_list = [5,2,4,3,7]
num_list.sort()
print(num_list)

# reverse : 순서 뒤집기
num_list.reverse()
print(num_list)

# clear : 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["A", 20, True]
print(mix_list)

# extend : 리스트 확장
num_list = [5,2,4,3,7]
num_list.extend(mix_list)
print(num_list)

