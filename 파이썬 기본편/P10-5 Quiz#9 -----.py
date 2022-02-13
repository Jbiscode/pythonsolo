from asyncio.base_futures import _FINISHED
from logging import exception


class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1 
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order > chicken :
            print("현재 {0}마리 까지만 주문 가능합니다.".format(chicken))
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호{0}] {1}마리 주문이 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order
            
        if chicken ==0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.") 
        
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
        
    except SoldOutError as err:
        print(err)
        break
        
    finally:
        print("찾아주셔서 감사합니다.")
    