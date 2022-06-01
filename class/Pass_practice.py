'''
    pass : 일단 넘어가게 해주는 역할
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
        # 일단 패스하고 실행된다
        pass

supply_depot = BuildingUnit("supply depot", 500, 20)

def game_start() :
    print("[알림] 새로운 게임을 시작합니다")

# 일단 넘어간다
def game_over() :
    pass

game_start()
game_over()