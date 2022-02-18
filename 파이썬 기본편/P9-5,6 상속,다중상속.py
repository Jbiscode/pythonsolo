# 일반유닛
class Unit:
    def __init__(self,name,hp):
        self.name = name                         ## 이것들이 멤버변수
        self.hp = hp
        # self.damage = damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))

# 공격유닛 
class Attack_Unit(Unit):   #  자녀클래스(부모클래스)         attack_unit 은 unit에서 상속받은 내용으로 만들어짐     
    def __init__(self,name,hp,damage):        # 공격유닛 생성
        # self.name = name
        # self.hp = hp
        Unit.__init__(self,name,hp)         ### 상속한 내용을 이렇게 써줘야함
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))
    
    def attack(self,location):
        print("{0}이 {1} 방향으로 공격합니다. [데미지 {2}]"\
            .format(self.name,location,self.damage))           # location 은 셀프없이 전달받은 location 을 쓰기때문에 self. 안붙혀도됨
    
    def damaged(self, damage):
        print("{0}이 {1} 피해를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        
        if self.hp > 0:
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        elif self.hp <= 0:
            print("{0} : 남은 체력은 {1} 입니다.".format(self.name,self.hp))    
            print("{} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능의 클래스            
class Flyable:   
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name,location,self.flying_speed))

# 공중 공격 유닛클래스        
class Flyable_Attack_Unit(Attack_Unit,Flyable):       #다중 상속
    def __init__(self,name,hp,damage,flying_speed):
        Attack_Unit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)
        
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일발사
valkyrie = Flyable_Attack_Unit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"11시")        