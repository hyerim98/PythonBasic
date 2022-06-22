# 튜플은 데이터의 값을 변경하지 못하는 자료구조이다

# 튜플 생성
my_variable = (1, ) # 1만 입력하면 정수로 인식
t = 1, 2, 3, 4 # 괄호가 없어도 튜플로 인식
print(type(my_variable))
print(type(t))


# 튜플 -> 리스트로 변경
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest))

# 리스트 -> 튜플로 변경
interest = tuple(interest)
print(type(interest))


# 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)


# range 함수를 이용하여 튜플 생성 
even = tuple(range(2, 100, 2))
print(even)
