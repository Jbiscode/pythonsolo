# 퀴즈 3) 사이트별로 비밀번호를 만들어주는 프로그램 작성

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2 : 처음 만나는 점 이후부분은 제외  -> naver 
# 규칙3 : 남은 글자중 처음 세자리 +글자갯수 +글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비번: nav51!

url = "http://naver.com"
url1 = url.replace("http://","")       #규칙 1
url1 = url1[0:url1.index(".")]         # url1[0:5]는 0~5직전까지
print(url1)

password = url1[:3]    +    str(len(url1))    +    str(url1.count("e"))    +   "!" 
# len(url1),url1.count("e")는 정수니까 문자를 합치기위해 앞에 str을 해서 ★문자화해준다★

print(password)
print(f"나의 {url}의 비밀번호는 {password}입니다.")
print("나의 {0}의 비밀번호는 {1}입니다.".format(url,password))