'''
    50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

    조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해진다
    조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 한다

    (출력문 예제)
    [0] 1번째 손님 (소요시간 : 15분)
    [] 2번째 손님 (소요시간 : 50분)
    [0] 3번째 손님 (소요시간 : 5분)
    ...
    [] 50번째 손님 (소요시간 : 16분)

    총 탑승 승객 : 2분
'''

from random import *

index = 1
count = 0


while index <= 50 :
    check = ""

    customer_time = randint(5, 50)

    # 매칭 성공
    if customer_time <= 15 :
        check = "O"
        count+=1
    
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)" .format(check, index, customer_time))

    index+=1


print("총 탑승 승객 : {0}명" .format(count))
