'''
 내장 함수 : import해서 사용하지 않아도 됨
    * input : 사용자 입력을 받는 함수
    * dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

    list of python builtins 구글링하면 내장 함수들 목록 나옴
'''

str = input("input >> ")

# 문자열 내장 함수 목록
print(dir(str))

lst = [1, 2, 3]
# 리스트 내장 함수 목록
print(dir(lst))