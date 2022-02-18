#__init__ 은 파이썬에서 쓰이는 생성자      클래스로부터 만들어지는 것들을 객채라고함

class unit:
    def __init__(self,name,hp,damage):
        self.name = name                         ## 이것들이 멤버변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))
        
m1 = unit("마린",40,5)
m2 = unit("마린",40,5)


## 멤버변수를 외부에서 쓰기   
# 레이스 : 공중유닛 , 비행기, 특수능력 : 클로킹(상대방에게 보이지않음)
wr = unit("레이스",80,5)      #레이스  
print("유닛이름 : {0}, 공격력 : {1}".format(wr.name,wr.damage))       # 클래스 외부에서 self. 대신 wr.을 써서 멤버변수에 접근할 수 있다.


#마인드컨트롤로 레이스를 빼았았다고 가정
wr2 = unit("빼앗은 레이스",80,5)
wr2.clocking = True

if wr2.clocking == True:            # wr2는 클래스외부에서 클로킹 설정을한것이기떄문에 wr1은 클로킹이 안된다.(확장을 한 객채에만 적용됨)
    print("{0}는 현재 클로킹 상태입니다.".format(wr2.name))
    