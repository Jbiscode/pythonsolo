# 출석번호가 1,2,3,4     앞에 100을 추가하기로함 e.g) 101,102,103,104
학생 = [1,2,3,4,5]                         # [] 리스트
print(학생)
학생 = [i +100 for i in 학생]          # i에 100을 추가, i는 학생에있는 것
print(학생)
print("------------------------------------------------------------------")

#################################################################################

# 이름을 길이로 변환
학생1 = ["Iron man","Thor","I am groot"]
print(학생1)
학생1 = [len(i) for i in 학생1]
print(학생1)

################################################################

# 학생 이름을 대문자로 변환
학생2 = ["Iron man","Thor","I am groot"]
print(학생2)
학생2 = [i.upper() for i in 학생2]
print(학생2)