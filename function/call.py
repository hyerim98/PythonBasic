# 함수 생성
def open_account():
    print("새로운 계좌가 생성되었습니다")

# 함수 호출
open_account()

# -----------------------------------------------------------------------------
# 함수 사용

# 입금
def deposit(balance, money) :
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다" .format(balance + money))
    return balance + money

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


balance = 0
balance = deposit(balance, 1000)
print(balance)


commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다" .format(commission, balance))


# -------------------------------------------------------------------
# 함수의 기본값
def profile1(name, age=17, main_lang="Python") :
    print("이름 : {0}, 나이 : {1}, 주 사용언어 : {2}" .format(name, age,main_lang))

profile1("AAA")
profile1("BBB")

# -------------------------------------------------------------------
# 함수의 키워드값
def profile2(name, age, main_lang) :
    print(name, age, main_lang)

profile2(name="CCC", main_lang="Java", age=25)
profile2(main_lang="Java", age=23, name="DDD")

# --------------------------------------------------------------------
# 함수 가변인자
def profile3(name, age, *language) : # *language : 가변인자
    print("이름 : {0}, 나이 : {1}\t" .format(name, age), end = " ")
    for lang in language :
        print(lang + " ", end = " ")
    print()

profile3("EEE", 30, "swift", "kotlin", "C", "C++")
profile3("FFF", 33, "Java", "C++")

