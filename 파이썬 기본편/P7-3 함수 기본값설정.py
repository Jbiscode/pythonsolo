def profile(name,age,main_lang):
    print("-------------\n이름 : {0} \n나이 : {1} \n주 사용 언어 : {2}\n-------------"\
          .format(name,age,main_lang)) #줄 이어쓸땐 \ 하고 엔터
    
profile("사재빈",27,"")
profile("사혜지",28,"한국어")


# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age = 27, main_lang = "파이썬"):      # 입력하지않으면 옆에있는 입력된것이 기본값이됨
    print("-------------\n이름 : {0} \n나이 : {1} \n주 사용 언어 : {2}\n-------------"\
          .format(name,age,main_lang))
    
profile("이사") 
    