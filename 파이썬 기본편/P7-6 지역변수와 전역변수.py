# 지역변수 = 함수내에서만 이용되는 변수, 함수가 호출될때 이용됐다가 호출안되면 안쓰임
# 전역변수 = 프로그램 내에서 어디서든지 이용되는 변수

gun = 10

##전역함수(코드 관리가 힘들어서 잘안씀)
# def checkpoint(군인):  
#     global gun                      #global로 전역함수 이용
#     gun = gun - 군인
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

def checkpoint1(gun,군인):  
    gun = gun - 군인
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
    
print("전체 총 : {0}".format(gun))
gun = checkpoint1(gun,2)               #함수 안으로 값을 넣었다가 뺌
print("남은 총 : {0}".format(gun))