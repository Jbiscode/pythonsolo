
# 일반유닛
class unit:
    def __init__(self,name,hp,damage):
        self.name = name                         ## 이것들이 멤버변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))

# 공격유닛 
class attack_unit:
    def __init__(self,name,hp,damage):        # 공격유닛 생성
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))
    
    def attack(self,location):
        print("{0}이 {1} 방향으로 공격합니다. [데미지 {2}]"\
            .format(self.name,location,self.damage))           # location 은 셀프없이 전달받은 location 을 쓰기때문에 self. 안붙혀도됨
    
    def damaged(self, damage):
        print("{0}이 {1} 피해를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        
        if self.hp >= 0:
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        elif self.hp <= 0:    
            print("{} : 파괴되었습니다.".format(self.name))
        
        
m1 = attack_unit("마린",40,5)
m1.attack("11시")
m1.damaged(10)
m1.damaged(30)