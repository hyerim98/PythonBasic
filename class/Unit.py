'''
    1. 클래스 생성자 만드는 법
    2. 생성된 인스턴스에 변수를 추가하여 사용 가능
'''

# 일반 유닛
class Unit :
    # 생성자
    # self : 자기 자신
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        
        print("{0} 유닛 생성".format(name))
        print("체력 : {0}, 공격력 : {1}".format(hp, damage))

marine1 = Unit("marine", 40, 5)
marine2 = Unit("marine", 50, 10)
tank = Unit("tank", 150, 35)

wraith1 = Unit("wraith", 80, 5)
# 멤버 변수 사용
print("name : {0}, attack : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("wraith", 80, 5)
# 객체에 외부에서 추가로 변수를 생성하여 사용 가능
wraith2.clocking = True

if wraith2.clocking == True :
    print("{0}는 현재 클로킹 상태".format(wraith2.name))
