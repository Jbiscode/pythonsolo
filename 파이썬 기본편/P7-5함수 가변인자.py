# 가변인자를 이용한 함수호출

# def profile(name, age, lang1, lang2="", lang3="", lang4="", lang5=""):
#     print("이름 : {0} \t나이 : {1}\t".format(name,age),end = " ")  # end = " "를 넣으면 없을땐 줄바꿈이지만
#                                                                   # 있으면 줄안바꾸고 같은줄에 이어불러옴
#     print(lang1, lang2, lang3, lang4, lang5)
    
    
def profile(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end =" ")
    for lang in language:
        print(lang,end=" ")
    print()
        
profile("유재석",20,"파이썬","자바","씨플","씨플플","쓰기") 
profile("김태호",23,"파이썬","자바") 