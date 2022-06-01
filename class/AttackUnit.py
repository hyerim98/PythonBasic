'''
    1. 상속
    2. 메소드 오버라이딩
'''

# 일반 유닛
class Unit :
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동 [속도 : {2}]" .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit) : # (상속받을 클래스)
    # 생성자
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage) :
        print("{0} : {1} 데미지".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴".format(self.name))

firebat1 = AttackUnit("firebat", 50, 20, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 비행 [속도 {2}]"\
            .format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable) : # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)
    
    # 메소드 오버라이딩
    def move(self, location) :
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "5시") 


# 메소드 오버라이딩
vulture = AttackUnit("vulture", 80, 10, 20)
battleCruiser = FlyableAttackUnit("battleCruiser", 500, 25, 3)

vulture.move("11시")
#battleCruiser.fly(battleCruiser.name, "9시")
battleCruiser.move("9시")