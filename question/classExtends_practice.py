class Car :
    def __init__(self, wheel, price) :
        self.wheel = wheel
        self.price = price

    def info(self) :
        print('바퀴 수 : {0}'.format(self.wheel))
        print('가격 : {0}'.format(self.price))



class Bike(Car) :
    def __init__(self, wheel, price, oper):
        super().__init__(wheel, price)
        self.oper = oper

    def info(self) :
        super().info()
        print('구동계 : {0}'.format(self.oper))



class Car2(Car) :
    def __init__(self, wheel, price):
        super().__init__(wheel, price)



bicycle = Bike(2, 100, "AAA")
print(bicycle.wheel)
print(bicycle.oper)
bicycle.info()

car = Car2(4, 1000)
car.info()

