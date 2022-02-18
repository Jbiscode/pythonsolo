# # while
# 고객 = "사재빈"
# index = 5
# while index >= 1:
#     print("{0}님의 커피가 준비되었습니다. 알람이 {1}회 남았습니다.".format(고객,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분합니다.")
# ###########################################################################

# customer = "토르"
# index = 1
# while index < 1000:
#     print("{0},커피가 준비되었습니다. 호출{1}회".format(customer,index))
#     index +=1
#     if index >= 500:
#         print("끝") 
# ############################################################################

# customer = "토르"
# index = 1
# while True:
#     print("{0},커피가 준비되었습니다. 호출{1}회".format(customer,index))
#     index +=1       

customer = "사재빈"
person = ""

while person != customer:          #앞에 person을 정의해주고 사용해야함 지정안해주면 오류
    print("{0}님 커피가준비되었습니다.".format(customer))
    person = input("이름이 어떻게되세요?")