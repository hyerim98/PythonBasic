'''
    * lambda 사용법
        - lambda 변수 : 표현식
'''

# lamda 적용 전
def mul(x, y = 7) :
    return x * y

print(mul(5))


# lamda 적용 후
mul = lambda x : x * 7
print(mul(5))