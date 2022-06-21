# " " 출력
print('신씨가 소리질렀다. \"도둑이야\"')

# sep 사용
print('naver', 'daum', 'google', 'chrome', sep='/')

# end 사용
print('first ', end="")
print('second')

# type 사용 : 데이터 타입을 판별
a = "129"
print(type(a))

# 문자열 출력
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))

print("이름: {0} 나이: {1}" .format(name1, age1))
print("이름: {0} 나이: {1}" .format(name2, age2))

print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
