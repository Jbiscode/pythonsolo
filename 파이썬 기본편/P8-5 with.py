# with를 사용하면 close를 안해도됨

import pickle

with open("profile.pickle","rb") as profile_file:   #프로필 피클을 열어서, 프로필파일에 저장을하고
    print(pickle.load(profile_file))                # 파일을 피클 로드로 불러온것
    
    
# 피클을 사용하지 않고 일반 파일을 with를 이용해서 열기
with open("study.txt","w",encoding = "utf8") as study_file:
    study_file.write("파이썬을 공부해보자")
    
with open("study.txt","r",encoding = "utf8") as study_file:
    print(study_file.read())