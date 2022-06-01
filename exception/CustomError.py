# 사용자 정의 에러(Exception을 상속받아야 함)
class BigNumberError(Exception) :
    def __init__(self, msg) :
        self.msg = msg

    # err로 print되는 문장
    def __str__(self) :
        return self.msg

try :
    print("한 자리 숫자 나누기 전용 계산기")

    num1 = int(input("num1 : "))
    num2 = int(input("num2 : "))

    # 한 자리를 입력받으면 Error 발생시키기
    if num1 >= 10 or num2 >= 10 :
        raise BigNumberError("입력 값 : {0}, {1}".format(num1, num2))

    # 정상처리면 실행되는 문장(에러가 발생되면 처리되지 않는다)
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError :
    print("잘못된 값을 입력 > 한 자리 숫자만 입력하세요")

except BigNumberError as err:
    print("한자리 숫자만 입력해야함")
    print(err)

# finally : 정상처리든지 에러 발생이든지 반드시 실행되는 구문
finally :
    print("이용 종료")