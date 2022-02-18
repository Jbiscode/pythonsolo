print("파이썬","자바",sep =",",end = "? ")
print("무엇이 더 재밌을까요?")

import sys
print("파이썬","자바",file = sys.stdout)
print("파이썬","자바",file = sys.stderr)

# 시험 성적
scores = {"수학":0,"영어":50,"코딩":100}
for subject,score in scores.items():
    print(subject, score)
    print(subject.ljust(8),str(score).rjust(4),sep =":")      #ljust 왼쪽정렬  rjust 오른쪽정렬
    
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||") 
   
# 은행 대기순번표
# 001,002,003, ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))   #zfill(3) 3글자 공간을 가지고 숫자없는 앞엔 0으로 채워줌
    
# input 으로 받은 글자들은 항상 문자열로 저장됨
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 {} 입니다.".format(answer))
print("입력하신 값은 " + answer+ " 입니다.")