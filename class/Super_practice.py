'''
    super
        * 부모를 호출
        * 다중 상속일 경우에 사용하는 경우는 한 부모밖에 호출하지 않는다
          그러므로 각각의 부모를 호출하는 것이 좋다  
'''

class Unit :
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동 [속도 : {2}]" .format(self.name, location, self.speed))


class BuildingUnit(Unit) :
    def __init__(self, name, hp, speed):
        super().__init__(name, hp, speed) # 부모 클래스 호출


class AAA:
    def __init__(self) :
        print("AAA 생성자")

class BBB:
    def __init__(self) :
        print("BBB 생성자")

class CCC(AAA, BBB):
    def __init__(self):
        # super().__init__() # 다중 상속일 경우는 super가 한 부모밖에 호출을 하지 못한다
        AAA.__init__(self)
        BBB.__init__(self)

ccc = CCC()