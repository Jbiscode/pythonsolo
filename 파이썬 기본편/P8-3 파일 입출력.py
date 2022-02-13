## 파일 쓰기

score_file = open("score.txt","w",encoding = "utf")     # "w"는 쓰기  write   "a"는 덮어쓰기  append
print("수학  : 0", file = score_file)
print("영어  : 50", file = score_file)
score_file.close()

score_file = open("score.txt","a",encoding = "utf")    
score_file.write("과학  : 70") 
score_file.write("\n코딩  : 100")                    # .write 로 입력하면 따로 줄바꿈이 없어서 따로해야함
score_file.close()

## 파일 읽기
print("-#전체 파일을 읽어온다-------------------")

score_file = open("score.txt","r",encoding = "utf")
print(score_file.read())                            #전체 파일을 읽어온다
score_file.close()

print("-#줄별로 읽어온다-------------------")

score_file = open("score.txt","r",encoding = "utf")
print(score_file.readline())          #줄별로 읽기, 이렇게 하면 한줄 읽고 마우스커서를 다음줄로 이동 
print(score_file.readline())              
print(score_file.readline(),end="")   #줄바꿈을 안하고싶으면 print(score_file.readline(),end="")
print(score_file.readline())
score_file.close()

# 몇 줄인지 모르는 파일 모두 열때
print("---# 몇 줄인지 모르는 파일 모두 열때--1번째---------")

score_file = open("score.txt","r",encoding = "utf")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

print("---# 몇 줄인지 모르는 파일 모두 열때--2번째---------")

score_file = open("score.txt","r",encoding = "utf")
lines = score_file.readlines()
for line in lines:
    print(line,end="")

score_file.close()