# 함수 생성
def open_account():
    print("새로운 계좌가 생성되었습니다")

# 함수 호출
open_account()


# 입금
def deposit(balance, money) :
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다" .format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)


# 출금
def withdraw(balance, money) :
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다" .format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다 잔액은 {0}원 입니다" .format(balance))
        return balance

# 저녁에 출금
def withdraw_night(balance, money) :
    commission = 100
    return commission, balance - money - commission


commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다" .format(commission, balance))