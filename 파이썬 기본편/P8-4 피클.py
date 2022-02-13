# 피클 = 프로그램상 사용하고 있는 데이터를 파일형태로 저장하는것

import pickle    

#쓰기
profile_file = open("profile.pickle", "wb")    #피클을 이용하려면 꼭 b 를 추가로 써야함(binary type)2진법
profile = {"이름":"박명수","나이":30,"취미":["가","나","다"]}
print(profile)
pickle.dump(profile,profile_file)   # profile에 있는 정보를 profile_file에 저장
profile_file.close()

# 읽기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
