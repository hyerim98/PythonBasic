try :
    print("한 자리 숫자 나누기 전용 계산기")

    num1 = int(input("num1 : "))
    num2 = int(input("num2 : "))

    # 한 자리를 입력받으면 Error 발생시키기
    if num1 >= 10 or num2 >= 10 :
        raise ValueError

    # 정상처리면 실행되는 문장(에러가 발생되면 처리되지 않는다)
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError :
    print("잘못된 값을 입력 > 한 자리 숫자만 입력하세요")