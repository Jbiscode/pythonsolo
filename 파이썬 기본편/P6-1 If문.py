# 날씨 = "비"
# if 조건:
#     실행 명령문

from pdb import Restart


날씨 = input("오늘 날씨는 어떤가요? (맑음,미세먼지,비,눈 中)    ")
if 날씨 == "비" or "눈":
    print("우산을 챙기세요")
elif 날씨 =="미세먼지":
    print("마스크를 챙기세요")
else:
    print("아무것도 필요없음")


기온 = int(input("기온은 어때요?"))
if 기온 >= 30:
    print("에어컨 트세요")
elif 기온 >= 10 and 기온 < 30:
    print("날씨가 좋네요")
elif 0<= 기온 <10:
    print(" 외투를 챙기세요")
else:
    print("너무 춥네요 나가지마세요.")