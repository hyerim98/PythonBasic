'''
    <예외>

    try:
        실행 코드
    except:
        예외가 발생했을 때 수행할 코드
    else:
        예외가 발생하지 않았을 때 수행할 코드
    finally:
        예외 발생 여부와 상관없이 항상 수행할 코드
'''

# try - except 예외처리
per = ["10.31", "", "8.00"]
perToFloat = []

for i in per :
    try :
        v = float(i)
    except :
        v = 0
    perToFloat.append(v)

print(perToFloat)


# try - except - else - finally 예외처리
for i in per :
    try :
        print(float(i))
    except :
        print(0)
    else :
        print('v의 값은 0이 아니다')
    finally :
        print('변환 완료')
    


# 특정 예외만 처리
try :
    num = 3 / 0
except ZeroDivisionError as err :
    print(err) # 예외 메세지
    print('0으로 나누면 안되요')


