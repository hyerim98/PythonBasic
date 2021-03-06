'''
    조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 경우는 ValueError로 처리
            출력 메시지 : "잘못된 값을 입력하였습니다"
    조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
            치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
            출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다"
'''

class SoldOutError(Exception) :
    def __init__(self, msg) :
        self.msg = msg

    def __str__(self) :
        return self.msg

chicken = 10
waiting = 1

while(chicken > 0) :
    try :
        orderChicken = int(input("주문 할 치킨 개수 : "))
    
        if orderChicken <= 0 :
            raise ValueError

        if chicken < orderChicken :
            raise SoldOutError("현재 {0}마리 주문가능합니다".format(chicken))

        print("[대기번호 : {0}] 주문이 완료되었습니다".format(waiting))
        waiting += 1
        chicken -= orderChicken

    except ValueError :
        print("잘못된 값을 입력하였습니다")
    
    except SoldOutError as err :
        print(err)
        print("재고가 부족합니다")

    finally :
        print("감사합니다")

print("재고가 소진되어 더 이상 주문을 받지 않습니다")

    