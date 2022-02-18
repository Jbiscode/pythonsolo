사물함 = {3:"유재석",100:"김태호"}       # 키key : 값value
#print(사물함[3])
#print(사물함[100])

#print(사물함.get(3))
#print(사물함[5])                     []는 없으면 오류뜨고 바로종료
print(사물함.get(5))             #    .get 써서 없으면 None뜨고 계속
print(사물함.get(5,"사용가능"))   #    None말고 찾기 실패시 지정멘트도 가능
print("hi")

print(3 in 사물함)
print(5 in 사물함)

사물함 = {"A-3":"유재석","B-100":"김태호"}
print(사물함["A-3"])
print(사물함["B-100"])

# 새 손님
print(사물함)
사물함["A-3"] = "김종국"
사물함["C-20"] ="조세호"
print(사물함)

# 간 손님
del 사물함["A-3"]
print(사물함)

# key 들만 출력
print(사물함.keys())

# value 들만 출력
print(사물함.values())

#key,value 모두출력
print(사물함.items())

#모두 지우기
사물함.clear()
print(사물함)