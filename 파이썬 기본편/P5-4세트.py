# 집합 {set}
# 중복안됨, 순서없음
my_set = {1,2,3,3,3,3}
print(my_set)

java = {"1","2","3"}
python = set(["1","4"])

# 교집합 (java와 python 개발자)
print(java&python)
print(java.intersection(python))

# 합집합 (java 나 python 중 할줄아는사람)
print(java | python)
print(java.union(python))

# 차집합 (java는 할수있지만 python은 모르는사람)
print(java - python)
print(java.difference(python))

# 파이썬 할줄아는사람 추가
python.add("2")
print(python)

# 자바를 까먹은사람 
java.remove("2")
print(java)