'''
    try - except : 에러 처리
'''
try :
    print("나누기 전용 계산기")

    num1 = int(input("num1 : "))
    num2 = int(input("num2 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# 숫자가 아닌 값 입력 받음
except ValueError :
    print("숫자가 아닌 다른 값이 입력되었습니다")

# 나누기 0을 입력 받음
except ZeroDivisionError as err :
    print(err)

# Java : catch(Exception e)로 에러 처리하는 것(명확한 에러가 아닌 모든 에러 검출)
except Exception as err:
    print("알 수 없는 에러가 발생")
    print(err)