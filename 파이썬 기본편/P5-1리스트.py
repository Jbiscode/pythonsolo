# 리스트 []

# 지하철 칸별로 10명 20명 30명
# subway1=10
# subway2=20
# subway3=30

subway=[10,20,30]
print(subway)

subway=["유재석","조세호","박명수"]
print(subway)


# 조세호가 몇번째 칸에 타고있는가
print(subway.index("조세호"))

# 하하가 다음정류장에서 다음칸에탐
subway.append("하하")       #append는 맨마지막에 붙힘
print(subway)

#  정형돈을 유재석/조세호 사이에 태움
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)


subway=["유재석","정형돈","조세호","박명수"]
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도가능
num_list =[5,3,4,1,2]
num_list.sort()
print(num_list)

#순서뒤집기
num_list.reverse()
print(num_list)

#모두지우기
num_list.clear()
print(num_list)

#리스트확장
num_list=[5,2,4,3,1]
mix_list=["유재석",20,True]
num_list.extend(mix_list)
print(num_list)

