# 클래스 생성1
class Human :

    def __init__(self, name, age, gender) :
         self.name = name
         self.age = age
         self.gender = gender

    def __del__(self) :
        print('클래스 소멸자')

    def setInfo(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def who(self) :
        print('이름: {0}, 나이: {1}, 성별: {2}'.format(self.name, self.age, self.gender))


areum = Human('AAA', 25, 'woman')
areum.who()
areum.setInfo('BBB', 30, 'man')
areum.who()

del(areum)




# 클래스 생성2
class Stock :

    def __init__(self, name, code, per, pbr, dividend) :
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name) :
        self.name = name

    def set_code(self, code) :
        self.code = code

    def set_per(self, per) :
        self.per = per

    def set_pbr(self, pbr) :
        self.pbr = pbr

    def set_dividend(self, dividend) :
        self.dividend = dividend

    def get_name(self) :
        return self.name

    def get_code(self) :
        return self.code

samsumg = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
name, code = samsumg.get_name(), samsumg.get_code()
print(name, code)

samsumg.set_per(12.75)


hyundai = Stock('현대차', '005380', 8.70, 0.35, 4.27)
lg = Stock('LG전자', '066570', 317.34, 0.69, 1.37)

# 리스트에 객체 넣기
list = [samsumg, hyundai, lg]

for i in list :
    print(i.get_code(), i.per)






import random

# 클래스 생성3
class Account :
    # 클래스 변수
    account_count = 0

    def __init__(self, name, balance) :
        self.deposit_count = 0

        self.dep_history = []
        self.with_history = []

        self.name = name
        self.balance = balance
        self.bank = 'SC제일은행'

        n1 = str(random.randint(0, 999)).zfill(3)
        n2 = str(random.randint(0, 99)).zfill(2)
        n3 = str(random.randint(0, 999999)).zfill(6)

        self.accountNum = n1 + '-' + n2 + '-' + n3

        # 클래스 변수
        Account.account_count += 1 

    # 클래스 메서드
    @classmethod
    def get_account_num(cls) :
        print(cls.account_count)

    
    def deposit(self, money) :
        if money <= 0 :
            print('금액 오류')
            return

        self.deposit_count += 1

        if(self.deposit_count % 5 == 0) :
            self.balance += self.balance * 1.01

        self.balance += money
        self.dep_history.append(money)
        print('입금 완료')

        return self.balance


    def deposit_history(self) :
        for amount in self.dep_history :
            print(amount)


    def withdraw(self, money) :
        if self.balance < money :
            print('잔액 부족')
            return

        self.balance -= money
        self.with_history.append(money)
        print('출금 완료')

        return self.balance


    def withdraw_history(self, ) :
        for amount in self.with_history :
            print(amount)

    
    def display_info(self) :
        print('은행이름: ', self.bank)
        print('예금주: ', self.name)
        print('계좌번호: ', self.accountNum)
        print('잔고: ', self.balance)



account1 = Account('AAA', 10000)
print(account1.name)
print(account1.balance)
print(account1.bank)
print(account1.accountNum)


account2 = Account('BBB', 1000000)

account3 = Account('CCC', 30000)

# 클래스명.함수명 으로 접근
Account.get_account_num()
# 인스턴스명.함수명 으로 접근(@classmethod 사용)
account2.get_account_num()


account_list = [account1, account2, account3]

for b in account_list :
    if(b.balance >= 1000000) :
        b.display_info()
    

